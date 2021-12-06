import build

sources = [
        '../mercury/source/main.cpp',
	'../mercury/source/common.cpp',
	'../mercury/source/init.cpp',
	'../mercury/source/lighting.cpp',
	'../mercury/source/logger.cpp',
	'../mercury/source/model.cpp',
	'../mercury/source/mouse_bus.cpp',
	'../mercury/source/rendering.cpp',
	'../mercury/source/shader.cpp',
	'../mercury/source/transform.cpp',
	'../mercury/source/engine/camera.cpp',
	'../mercury/source/engine/monitors.cpp',
	'../mercury/source/engine/skybox.cpp',
	'../mercury/source/mesh/basic.cpp',
	'../mercury/source/mesh/cuboid.cpp',
	'../mercury/source/mesh/sphere.cpp',
	'../mercury/source/physics/physics.cpp',
	'../mercury/source/ui/button.cpp',
	'../mercury/source/ui/pure_rect.cpp',
	'../mercury/source/ui/rect.cpp',
	'../mercury/source/ui/text.cpp',
	'../mercury/source/ui/ui_layer.cpp',
	'../mercury/glad/glad.c'
]

includes = [
        '../mercury',
        '../mercury/glad',
        '../mercury/assimp/include',
	'../mercury/thirdparty/freetype2/include',
	'../mercury/thirdparty/glm',
	'/usr/include/bullet'
	# '/usr/local/include/bullet'
]

libraries = [
        'ncurses',
        'dl',
        'glfw',
        'freetype',
        'assimp',
        'BulletCollision',
        'BulletDynamics',
        'LinearMath'
]

# TODO: add options to define macros
build = build.Build('mercury', 'mercury_main', sources, includes,
        libraries, '-DMERCURY_SOURCE_DIR=\\\"../mercury\\\"')
build.run()
