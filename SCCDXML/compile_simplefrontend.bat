@echo off
python sccd_compiler-master\python_sccd_compiler\sccdc.py Tests\FrontEnd\frontend_controller.xml -o Tests\FrontEnd\frontend_controller.py -p gameloop
python sccd_compiler-master\python_sccd_compiler\sccdc.py Tests\FrontEnd\button_controller.xml -o Tests\FrontEnd\button_controller.py -p gameloop
python sccd_compiler-master\python_sccd_compiler\sccdc.py Tests\FrontEnd\instance_controller.xml -o Tests\FrontEnd\instance_controller.py -p gameloop
python sccd_compiler-master\python_sccd_compiler\sccdc.py Tests\FrontEnd\browse_window_controller.xml -o Tests\FrontEnd\browse_window_controller.py -p gameloop