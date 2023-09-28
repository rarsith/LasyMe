from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot
from lasy_ops.tiny_ops.tasks_ops import TinyOps
from lasy_ui.custom_widgets.task_entry_item_widget import TaskEntityWDG
from lasy_ops.tdb_attributes_paths import TasksAttributesPaths
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ui.custom_widgets.task_viewer_widget import ExitingTasksViewerWDG
from lasy_ops.tdb_priorities import Priorities
from lasy_ops.tdb_statuses import Statuses


class ExitingTasksViewerBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.task_viewer_trw = ExitingTasksViewerWDG()

        self.show_me_tasks_of_today_btn = QtWidgets.QPushButton("TASKS FOR TODAY")
        self.show_me_tasks_of_today_btn.setCheckable(True)
        self.show_me_tasks_of_today_btn.setChecked(True)

        self.show_done_tasks_btn = QtWidgets.QPushButton("Show DONE Tasks")
        self.show_done_tasks_btn.setCheckable(True)

        self.by_prio_btn = QtWidgets.QPushButton("by Prio")
        self.by_prio_btn.setCheckable(True)

        self.by_status_btn = QtWidgets.QPushButton("by Status")
        self.by_status_btn.setCheckable(True)

        self.by_created_btn = QtWidgets.QPushButton("by Created")
        self.by_created_btn.setCheckable(True)

        self.by_end_date_btn = QtWidgets.QPushButton("by DDate")
        self.by_end_date_btn.setCheckable(True)
        self.by_end_date_btn.setChecked(True)

        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.refresh_btn.setMinimumHeight(30)

        self.filter_by_buttons_group = QtWidgets.QButtonGroup()
        self.filter_by_buttons_group.addButton(self.by_prio_btn)
        self.filter_by_buttons_group.addButton(self.by_end_date_btn)
        self.filter_by_buttons_group.addButton(self.by_created_btn)
        self.filter_by_buttons_group.addButton(self.by_status_btn)

    def create_layout(self):
        buttons_layout = QtWidgets.QGridLayout()
        buttons_layout.addWidget(self.show_me_tasks_of_today_btn, 0, 0, 1, 4)
        buttons_layout.addWidget(self.show_done_tasks_btn, 1, 0, 1, 4)
        buttons_layout.addWidget(self.by_end_date_btn, 2, 0)
        buttons_layout.addWidget(self.by_created_btn, 2, 1)
        buttons_layout.addWidget(self.by_status_btn, 2, 2)
        buttons_layout.addWidget(self.by_prio_btn, 2, 3)

        task_viewer_layout = QtWidgets.QVBoxLayout()
        task_viewer_layout.addLayout(buttons_layout)
        task_viewer_layout.addWidget(self.task_viewer_trw)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_viewer_layout)
        main_layout.addWidget(self.refresh_btn)


class ExistingTasksViewerCore(ExitingTasksViewerBuild):
    task_document_retrieval = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(ExistingTasksViewerCore, self).__init__(parent)

        self.tiny_ops = TinyOps()
        self.tiny_attr_definitions = TaskAttributesDefinitions()
        self.tiny_attr_paths = TasksAttributesPaths(self.tiny_attr_definitions)

        self.prios = []
        self.statuses = []
        self.tags = []

        # self.cache_database()

        self.populate_tasks()
        self.create_connections()

    def create_connections(self):
        self.task_viewer_trw.itemPressed.connect(self.retrieve_task_doc)
        self.task_viewer_trw.itemPressed.connect(lambda: self.get_view_entries(6))
        self.refresh_btn.clicked.connect(self.refresh_all)
        self.filter_by_buttons_group.buttonClicked.connect(self.get_current_filter)
        # self.show_me_tasks_of_today_btn.clicked.connect(self.get_tasks_for_today)
        self.show_me_tasks_of_today_btn.clicked.connect(self.populate_tasks)
        self.show_done_tasks_btn.clicked.connect(self.populate_tasks)

    def get_tasks_for_today(self):
        is_button_checked = self.show_me_tasks_of_today_btn.isChecked()
        if is_button_checked:
            criteria_def = self.define_query_criteria()
            self.populate_by_criteria(criteria_def)
            get_current_content_ids = self.get_view_entries(6)
            extracted_tasks_for_today = self.tiny_ops.get_tasks_by_remaining_time(tasks_ids=get_current_content_ids,
                                                                                 reference_max=3)
            self.populate_by_ids_list(extracted_tasks_for_today)

        else:
            criteria_def = self.define_query_criteria()
            self.populate_by_criteria(criteria_def)

    def cache_database(self):
        self.all_documents_cache = self.tiny_ops.get_all_documents(ids=True)
        return self.all_documents_cache

    def get_current_filter(self):
        checked_button = self.filter_by_buttons_group.checkedButton()
        if checked_button:
            if checked_button.text() == "by Prio":
                self.sort_by_prio()
            elif checked_button.text() == "by Status":
                self.sort_by_status()
            elif checked_button.text() == "by Created":
                self.sort_by_creation_date()
            else:
                self.sort_by_end_date()
        else:
            return

    def populate_tasks_custom(self, key_to_sort, descending=False):
        get_selected = self.keep_selected_buffer()

        get_current_content_ids = self.get_view_entries(6)
        all_documents = self.tiny_ops.get_docs_by_id(get_current_content_ids)
        sorted_tasks = dict(sorted(all_documents.items(), key=lambda item: item[1][key_to_sort], reverse=descending))

        self.task_viewer_trw.clear()
        for key, value in sorted_tasks.items():
            if value["parent"] == "root":
                root_item = self.task_viewer_trw.invisibleRootItem()
                self.add_custom_widget(root_item, task_id=key)
            self.task_viewer_trw.expandAll()

        self.restore_selected_buffer(get_selected)

    def define_query_criteria(self):
        criteria = dict()
        tags_bool = (len(self.tags) != 0)
        prio_bool = (len(self.prios) != 0)
        status_bool = (len(self.statuses) != 0)
        if any([tags_bool, prio_bool, status_bool]):
            if tags_bool:
                criteria[self.tiny_attr_definitions.tags] = self.tags
            if prio_bool:
                criteria[self.tiny_attr_definitions.prio] = self.prios
            if status_bool:
                criteria[self.tiny_attr_definitions.status] = self.statuses
        return criteria

    def populate_viewer(self, database_documents: dict):
        button_checked = self.show_done_tasks_btn.isChecked()
        get_selected = self.keep_selected_buffer()
        self.task_viewer_trw.clear()
        for key, value in database_documents.items():
            root_item = self.task_viewer_trw.invisibleRootItem()
            if not button_checked:
                if value["status"] != Statuses().done:
                    self.add_custom_widget(root_item, task_id=key)
            else:
                self.add_custom_widget(root_item, task_id=key)

        self.task_viewer_trw.expandAll()
        self.restore_selected_buffer(get_selected)


    def populate_by_criteria(self, criteria):
        get_selected = self.keep_selected_buffer()

        if len(criteria) != 0:
            all_documents = self.tiny_ops.get_docs_by_multiple_keys(criteria=criteria)
        else:
            all_documents = self.tiny_ops.get_all_documents(ids=True)

        if all_documents:
            self.task_viewer_trw.clear()

            is_button_checked = self.show_me_tasks_of_today_btn.isChecked()
            if is_button_checked:
                extracted_tasks_for_today = self.tiny_ops.get_tasks_by_remaining_time(tasks_ids=all_documents.keys(),
                                                                                      reference_max=3)
                self.populate_by_ids_list(extracted_tasks_for_today)
                self.restore_selected_buffer(get_selected)

            else:
                if len(criteria) != 0:
                    all_documents = self.tiny_ops.get_docs_by_multiple_keys(criteria=criteria)
                else:
                    all_documents = self.tiny_ops.get_all_documents(ids=True)

                self.populate_viewer(all_documents)

                # for key, value in all_documents.items():
                #     root_item = self.task_viewer_trw.invisibleRootItem()
                #     self.add_custom_widget(root_item, task_id=key)
                #
                #     self.task_viewer_trw.expandAll()
                #     self.restore_selected_buffer(get_selected)

        else:
            return

    def populate_by_ids_list(self, ids_list):
        all_documents = self.tiny_ops.get_docs_by_id(ids_list)
        if all_documents:
            self.populate_viewer(all_documents)
            # self.task_viewer_trw.clear()
            # for key, value in all_documents.items():
            #     root_item = self.task_viewer_trw.invisibleRootItem()
            #     self.add_custom_widget(root_item, task_id=key)
            #
            #     self.task_viewer_trw.expandAll()

        else:
            return

    @Slot(dict)
    def populate_tasks_by_prio(self, filter_name):
        self.prios = filter_name["prios"]
        criteria_def = self.define_query_criteria()
        self.populate_by_criteria(criteria_def)
        self.get_current_filter()

        return self.prios

    @Slot(dict)
    def populate_tasks_by_status(self, filter_name):
        self.statuses = filter_name["statuses"]
        criteria_def = self.define_query_criteria()
        self.populate_by_criteria(criteria_def)
        self.get_current_filter()

        return self.statuses

    @Slot(dict)
    def populate_tasks_by_tags(self, tag_package):
        self.tags = tag_package["tags"]
        criteria_def = self.define_query_criteria()
        self.populate_by_criteria(criteria_def)
        self.get_current_filter()

        return self.tags

    def get_all_documents_in_viewer(self):
        self.all_documents = self.tiny_ops.get_docs_by_id(self.all_items_in_viewer)
        return self.all_documents

    def populate_tasks_to_list(self, key_to_sort, order_ref=[]):
        # get_selected = self.keep_selected_buffer()

        get_current_content_ids = self.get_view_entries(6)
        all_documents = self.tiny_ops.get_docs_by_id(get_current_content_ids)
        sorted_tasks = dict(sorted(all_documents.items(), key=lambda item: order_ref.index(item[1][key_to_sort])))
        self.populate_viewer(sorted_tasks)

        # self.task_viewer_trw.clear()
        # for key, value in sorted_tasks.items():
        #     if value["parent"] == "root":
        #         root_item = self.task_viewer_trw.invisibleRootItem()
        #         self.add_custom_widget(root_item, task_id=key)
        #     self.task_viewer_trw.expandAll()
        #
        # self.restore_selected_buffer(get_selected)

    def keep_selected_buffer(self):
        selected_items = []
        for item in self.task_viewer_trw.selectedItems():
            text = item.text(6)
            selected_items.append(text)
        return selected_items

    def restore_selected_buffer(self, selected_items):
        for row_index in range(self.task_viewer_trw.topLevelItemCount()):

            item = self.task_viewer_trw.topLevelItem(row_index)

            if item:
                column_index = 6
                cell_value = item.text(column_index)

                if len(selected_items) != 0:
                    if cell_value == selected_items[0]:

                        item.setSelected(True)
                        break

    def populate_tasks(self):
        get_selected = self.keep_selected_buffer()

        criteria_def = self.define_query_criteria()
        self.populate_by_criteria(criteria_def)

        self.get_current_filter()

        self.restore_selected_buffer(get_selected)

    def clear_duplicates(self):
        get_current_content_ids = self.get_view_entries(6)
        all_documents = self.tiny_ops.get_docs_by_id(get_current_content_ids)
        self.populate_viewer(all_documents)

        # for key, value in all_documents.items():
        #     if value["parent"] == "root":
        #         root_item = self.task_viewer_trw.invisibleRootItem()
        #         self.add_custom_widget(root_item, task_id=key)
        #     self.task_viewer_trw.expandAll()

    def sort_by_end_date(self):
        self.populate_tasks_custom(self.tiny_attr_definitions.end_date_interval)

    def sort_by_creation_date(self):
        self.populate_tasks_custom(self.tiny_attr_definitions.datetime_created, descending=True)

    def sort_by_prio(self):
        priority_order = Priorities().all_priorities
        self.populate_tasks_to_list(key_to_sort=self.tiny_attr_definitions.prio, order_ref=priority_order)

    def sort_by_status(self):
        statuses_order = Statuses().all_statuses
        self.populate_tasks_to_list(key_to_sort=self.tiny_attr_definitions.status, order_ref=statuses_order)

    def get_view_entries(self, index):
        self.all_items_in_viewer = []

        def recursive_traversal(parent_item):
            for child in range(parent_item.childCount()):
                child_item = parent_item.child(child)
                self.all_items_in_viewer.append(int(child_item.text(index)))
                recursive_traversal(child_item)

        # Start the traversal from the top-level items
        for i in range(self.task_viewer_trw.topLevelItemCount()):
            top_level_item = self.task_viewer_trw.topLevelItem(i)
            self.all_items_in_viewer.append(int(top_level_item.text(index)))
            recursive_traversal(top_level_item)
        return self.all_items_in_viewer

    def retrieve_task_doc(self, item, column):
        if item is not None:
            text = item.text(6)
            task_doc = self.tiny_ops.get_doc_by_id(int(text))
            complete_task_emit = {}
            complete_task_emit["task_id_emit"] = text
            complete_task_emit["task_emit"] = task_doc
            self.task_document_retrieval.emit(complete_task_emit)
            return task_doc

    def add_custom_widget(self, parent_item, task_id):
        child_item = QtWidgets.QTreeWidgetItem(parent_item)

        custom_widget_container = TaskEntityWDG(task_id=task_id)
        title_text = custom_widget_container.get_task_title()
        custom_widget_container.get_progress_bar_amount()
        custom_widget_container.get_task_title()
        check_status = custom_widget_container.get_task_status()
        # if check_status == Statuses().done:


        custom_widget_container.get_task_prio()

        custom_widget_container.delete_btn.clicked.connect(self.delete_task)
        custom_widget_container.prio_cb.activated.connect(self.update_task_prio)
        custom_widget_container.status_cb.activated.connect(self.update_task_status)

        self.task_viewer_trw.setItemWidget(child_item, 0, custom_widget_container.prog_bar)
        self.task_viewer_trw.setItemWidget(child_item, 1, custom_widget_container.task_title_lb)
        self.task_viewer_trw.setItemWidget(child_item, 2, custom_widget_container.status_cb)
        self.task_viewer_trw.setItemWidget(child_item, 3, custom_widget_container.prio_cb)
        self.task_viewer_trw.setItemWidget(child_item, 4, custom_widget_container.delete_btn)

        child_item.setText(6, str(task_id))
        return child_item

    # This is still to be built (Drag and Drop taks onto eachother to create parent-child)
    def handle_item_dropped(self, parent_item, dropped_index, item):
        if parent_item is not None:
            specific_column_text = item.text(6)

            dropped_row = self.tree_widget.indexOfTopLevelItem(parent_item)

            print(f"Text from column 6 of the dropped item: {specific_column_text}")
            print(f"Item dropped onto row {dropped_row}")

    @Slot(str)
    def refresh_all(self):
        self.populate_tasks()

    def update_task_status(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        value_selected = sender_button.currentText()
        task_id = item.text(6)
        self.tiny_ops.update_task(int(task_id), self.tiny_attr_paths.status(value_selected))
        # if value_selected == Statuses().done:
        self.refresh_all()


    def update_task_prio(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        value_selected = sender_button.currentText()
        task_id = item.text(6)
        self.tiny_ops.update_task(int(task_id), self.tiny_attr_paths.priority(value_selected))

    def delete_task(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        task_id = item.text(6)
        self.tiny_ops.delete_task(int(task_id))
        self.refresh_all()


if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ExistingTasksViewerCore()
    test_dialog.show()
    sys.exit(app.exec_())
