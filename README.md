# pokemon-data
- Fetch individual Pokémon by ID
- Retrieve multiple Pokémon in bulk
- Clean dataclass-based models
- Zero configuration required

## Quick Start

```python
from pokemon_client import getPokemonById, getAllPokemon, getPokemonCount

# Get total Pokémon count
total = getPokemonCount()

# Fetch a specific Pokémon
pikachu = getPokemonById(25)
print(pikachu)
# ID: 25, NAME: pikachu, BASE_EXP: 112, HEIGHT: 4, WEIGHT: 60.0, IS_DEFAULT: True

# Get the first 151 Pokémon
pokemon = getAllPokemon(151)
```

## Only Requirements

```bash
pip install requests
```

## API Reference

### `getPokemonCount() -> int`
Returns the total number of Pokémon available in the API.

### `getPokemonById(i: int) -> Pokemon`
Fetches a single Pokémon by its ID (1-1025+).

### `getAllPokemon(limit: int) -> List[Pokemon]`
Retrieves multiple Pokémon. Omit `limit` to fetch all available Pokémon (warning: this takes a while!).

### `Pokemon` Dataclass
| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Pokédex number |
| `name` | str | Pokémon name |
| `base_experience` | int | Base XP yield |
| `height` | int | Height in decimeters |
| `weight` | float | Weight in hectograms |
| `is_default` | bool | Default form variant |

## License

This project uses data from [PokéAPI](https://pokeapi.co/), a free and open Pokémon API.
