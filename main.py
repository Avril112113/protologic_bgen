import json
from protologic_bgen import Bindings, Generator


if __name__ == "__main__":
	with open("protologic_bindings.json") as f:
		data = json.loads(f.read())

	bindings = Bindings().updateFromJson(data)
	Generator(bindings).generate()
