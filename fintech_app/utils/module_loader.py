import importlib
import os

class ModuleLoader:
    def __init__(self, base_path, base_class):
        self.base_path = base_path
        self.base_class = base_class

    def discover_modules(self):
        module_dir = os.path.join(os.getcwd(), self.base_path)
        return [name for name in os.listdir(module_dir)
                if os.path.isdir(os.path.join(module_dir, name))]

    def load_module(self, module_name):
        try:
            module = importlib.import_module(f"{self.base_path}.{module_name}")
            controller_class = getattr(module, 'Controller')
            return controller_class()
        except Exception as e:
            print(f"加载模块 {module_name} 失败: {str(e)}")
            return None