import yaml
yml = yaml.load(open('build.yml', 'r'))

with open('build.sh', 'w') as f:
    for y in yml['Tests'].get('Required'):
        f.write('cp -rf {} tests\n'.format(y))
    f.write ('cd tests\n')

    project_name = yml['Projects']['Name'][0]
    sub_name = '/{}'.format(yml['Projects']['SubName'][0]) if yml['Projects']['SubName'][0] else ''
    version = ':' + yml['Projects']['Version'][0] if yml['Projects'].get('Version','') else ''


    project_name = '{project_name}{sub_name}{version}'.format(project_name=project_name,
                                                                sub_name=sub_name,
                                                                version=version)
    f.write ('docker build -t {project_name} .\n'.format(project_name=project_name))

    volume = "mkdir {}\n.format".format(yml['Tests']['Volume'][0]) if yml['Tests']['Volume'][0] else ''
    if volume:
        volume_path = "-v `pwd`/{}/tmp".format(volume)
    else:
        volume_path = ""
    f.write ('docker run {volume_path} {project_name}\n'.format(volume_path=volume_path,
                                                             project_name=project_name))

