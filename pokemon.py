# https://pokeapi.co/api/v2/pokemon/{i}

import requests

from typing import List
from dataclasses import dataclass

POKEMON_COUNT = 0


@dataclass
class Pokemon:
  id: int
  name: str
  base_experience: int
  height: int
  weight: float
  is_default: bool
  
  def __str__(self):
    return f"ID: {self.id}, NAME: {self.name}, BASE_EXP: {self.base_experience}, HEIGHT: {self.height}, WEIGHT: {self.weight}, IS_DEFAULT: {self.is_default}"


def getPokemonCount() -> int:
  global POKEMON_COUNT
  
  res = requests.get("https://pokeapi.co/api/v2/pokemon").json()
  POKEMON_COUNT = res['count']
  return POKEMON_COUNT


def getPokemonById(i: int) -> Pokemon:
  res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
   
  return Pokemon(
    id=res['id'],
    name=res['name'],
    base_experience=res['base_experience'],
    height=res['height'],
    weight=res['weight'],
    is_default=res['is_default']
  )


def getAllPokemon(limit=POKEMON_COUNT) -> List[Pokemon]:
  global POKEMON_COUNT

  count = limit if limit != POKEMON_COUNT else POKEMON_COUNT

  print(f"Fetching {count} pokemon information...")

  pokemon = []
  for i in range(1, count + 1):
    p = getPokemonById(i)
    pokemon.append(p)
  
  return pokemon


def main():
  # Set global count variable
  getPokemonCount()
  
  pokemon = getAllPokemon(4)
  
  for p in pokemon:
    print(p)
    
main()