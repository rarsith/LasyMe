import os
import platform

class Envars:

    def set_environment_variable(self,env_var_name ,env_var_value):
        if not self.check_if_exists(env_var_name):
            os_name = platform.system()
            if os_name == 'Windows':
                # os.environ[env_var_name] = env_var_value
                os.system(f'setx {env_var_name} "{env_var_value}"')
                print(f'Set environment variable {env_var_name} to {env_var_value} on Windows.')

            elif os_name == 'Darwin':
                with open(os.path.expanduser("~/.bash_profile"), "a") as file:
                    file.write(f"export {env_var_name}='{env_var_value}'\n")
                print(f'Appended environment variable {env_var_name} to .bash_profile on macOS.')

            elif os_name == 'Linux':
                with open(os.path.expanduser("~/.bashrc"), "a") as file:
                    file.write(f"export {env_var_name}='{env_var_value}'\n")
                print(f'Appended environment variable {env_var_name} to .bashrc on Linux.')
            else:
                print(f'Unsupported operating system: {os_name}')

    def check_if_exists(self, env_var_name):
        return env_var_name in os.environ
