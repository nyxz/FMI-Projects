from cx_Freeze import setup, Executable

setup(
    name = "StarWars",
    version = "Beta v0.1",
    description = "Shooter",
    executables = [Executable("run_game.py")]
)
