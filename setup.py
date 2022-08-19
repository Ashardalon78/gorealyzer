import cx_Freeze

executables = [cx_Freeze.Executable("main.py",targetName="gorealyzer.exe")]

cx_Freeze.setup(
	name = "gorealyzer",
	options={"build_exe": {"packages":["numpy","matplotlib","pandas","tkinter","selenium","bs4","warnings","time","os"],
							"include_files":["resources"],
							'namespace_packages': ["mpl_toolkits"]}},
	executables = executables
	)