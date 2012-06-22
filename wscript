def set_options(opt):
  opt.tool_options("compiler_cxx")


def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.check_tool('node_addon')
    conf.check_cfg(package='opencv',
      atleast_version='2.3.1',
      libpath=[
        '/lib', '/usr/lib', '/usr/local/lib','/usr/local/include', 
        '/opt/local/include', '/opt/local/lib'],
      args='--cflags --libs',
      uselib_store='OPENCV', 
      mandatory=True)


def build(bld):
    obj = bld.new_task_gen("cxx", "shlib", "node_addon")
    obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
    # This is the name of our extension.
    obj.target = "opencv"
    obj.source = bld.glob('src/*.cc')
    obj.uselib = ['OPENCV']

