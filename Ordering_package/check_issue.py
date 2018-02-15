import glob
import pathlib
cwd = pathlib.Path.cwd()
import numpy


s_e_dir = str(pathlib.Path(cwd, 'safe_eliminations'))
sd_t_dir = str(pathlib.Path(cwd, 'sdopt_tearing'))
dirs = [s_e_dir,sd_t_dir]



def test_issue(module_names,contents):

    #issue when from [module x] import [function] where [function] has same name as a module
    test = 0
    possible_fails = []
    for m in module_names:
        for n in module_names:
            string = "from " + m + "import " + n
            possible_fails.append(string)

    for fail in possible_fails:
        if fail in contents:
            test += 1

    if test == 0:
        return False
    else:
        return True


has_issue = {}

for d in dirs:
    files = glob.glob(d+'\*.py')
    pyfiles = [f.split('\\')[-1] for f in files]
    # print(pyfiles)
    has_issue.update({d: numpy.zeros_like(pyfiles)})
    module_names = [f.split('.')[0] for f in pyfiles]

    for i,f in enumerate(files):
        # print(f)
        g = pyfiles[i]
        contents = open(f).read()
        for m in module_names:
            v1 = "import " + m
            v2 = "from " + m
            if v1 or v2 in contents:
                check = test_issue(module_names,contents)
                if check == True:
                    has_issue[d][i] = 1
                else:
                    has_issue[d][i] = 0

print(has_issue)