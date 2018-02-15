import glob
import pathlib
cwd = pathlib.Path.cwd()


s_e_dir = str(pathlib.Path(cwd,'safe_eliminations'))
sd_t_dir = str(pathlib.Path(cwd,'sdopt_tearing'))
dirs = [s_e_dir,sd_t_dir]

for d in dirs:
    files = glob.glob(d+'\*.py')
    pyfiles = [f.split('\\')[-1] for f in files]
    module_names = [f.split('.')[0] for f in pyfiles]

    for f in files:

        contents = open(f).read()
        for m in module_names:
            v1 = "import " + m
            v2 = "from " + m
            if v1 or v2 in contents:
                contents = contents.replace(v1, "import ."+m)
                contents = contents.replace(v2, "from ."+m)
        # with open('new_'+f, 'w') as outf:
        #     outf.write(contents)

