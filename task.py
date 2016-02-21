import sys
import yaml

def generate_build_task(destination="test"):
    TASK = {"test": "Tests", "build": "Build", "deploy": "Deploy"}
    yml = yaml.load(open('build.yml', 'r'))

    DESTINATION = destination
    TASK = yml[TASK[destination]]
    with open('build.sh', 'w') as f:
        for y in TASK.get('Required'):
            f.write('cp -rf {} {}\n'.format(y, DESTINATION))
        f.write ('cd {}\n'.format(DESTINATION))

        project_name = yml['Projects']['Name'][0]
        sub_name = '/{}'.format(yml['Projects']['SubName'][0]) if yml['Projects']['SubName'][0] else ''
        version = ':' + yml['Projects']['Version'][0] if yml['Projects'].get('Version','') else ''


        project_name = '{project_name}{sub_name}{version}'.format(project_name=project_name,
                                                                    sub_name=sub_name,
                                                                    version=version)
        build_string = 'docker build -t {project_name} .\n'.format(project_name=project_name)
        f.write (build_string)
        #print (TASK['Volume'])
        volume = "mkdir {}".format(TASK['Volume'][0]) if TASK['Volume'][0] else ''
        f.write(volume)
        f.write('\n')
        if volume:
            volume_path = "-v `pwd`/{}/tmp".format(volume)
        else:
            volume_path = ""
        run_string = 'docker run {volume_path} {project_name}\n'.format(volume_path=volume_path,
                                                                        project_name=project_name)
        #print (run_string)
        f.write (run_string)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            generate_build_task(sys.argv[1])
        except:
            print ("invalid task. Please input test or build or deploy")
    else:
        generate_build_task()
