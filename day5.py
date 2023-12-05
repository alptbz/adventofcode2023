from typing import List


class Seed:

    def __init__(self, num: int, length: int):
        self.length = length
        self.num = num


class RangeMap:

    def __init__(self, destination_from: int, source_from: int, length: int):
        self.length = length
        self.source_from = source_from
        self.destination_from = destination_from

    def min_source(self) -> int:
        return self.source_from

    def max_source(self) -> int:
        return self.source_from + self.length - 1

    def min_dest(self) -> int:
        return self.destination_from

    def max_dest(self) -> int:
        return self.destination_from + self.length - 1

    def match_source(self, source_num) -> bool:
        return self.min_source() <= source_num <= self.max_source()

    def match_dest(self, dest_num) -> bool:
        return self.min_dest() <= dest_num <= self.max_dest()

    def match_source_by_range(self, s_mi, l) -> bool:
        s_ma = s_mi + l - 1
        return not (self.max_source() < s_mi or self.min_source() > s_ma)

    def translate_range(self, s_mi, l):
        calc_min_source = max([s_mi, self.min_source()])
        calc_max_source = min([s_mi + l - 1, self.max_source()])
        assert calc_min_source < calc_max_source
        assert calc_max_source - calc_min_source > 0
        assert s_mi + l >= self.min_source()
        assert s_mi <= self.max_source()
        return self.translate(calc_min_source), self.translate(calc_max_source)

    def translate(self, source_num) -> int:
        return self.destination_from + (source_num - self.min_source())

    def translate_reverse(self, dest_num) -> int:
        return self.source_from + (dest_num - self.min_dest())

    def movement(self) -> int:
        return self.min_dest() - self.min_source()


class Mapper:

    def __init__(self, from_type: str, to_type: str):
        self.to_type = to_type
        self.from_type = from_type
        self.range_maps: List[RangeMap] = []

    def add(self, range_map: RangeMap):
        self.range_maps.append(range_map)

    def __str__(self):
        return f'{self.from_type} => {self.to_type} ({self.min_movement()} => {self.max_movement()})'

    def __repr__(self):
        return self.__str__()

    def min_movement(self) -> int:
        return min(x.movement() for x in self.range_maps)

    def max_movement(self) -> int:
        return max(x.movement() for x in self.range_maps)

    def map_dest(self, dest_num) -> int:
        compatible_range_mapper = [rm for rm in self.range_maps if rm.match_dest(dest_num)]
        if len(compatible_range_mapper) == 0:
            return dest_num
        else:
            return compatible_range_mapper[0].translate_reverse(dest_num)

    def map_source(self, source_num) -> int:
        compatible_range_mapper = [rm for rm in self.range_maps if rm.match_source(source_num)]
        if len(compatible_range_mapper) == 0:
            return source_num
        else:
            return compatible_range_mapper[0].translate(source_num)

    def map_source_to_range(self, s_mi, l) -> (int, int):
        compatible_range_mapper = [rm for rm in self.range_maps if rm.match_source_by_range(s_mi, l)]
        min_dest_values = [c.translate_range(s_mi, l)[0] for c in compatible_range_mapper]
        max_dest_values = [c.translate_range(s_mi, l)[1] for c in compatible_range_mapper]
        min_dest_values.append(s_mi)
        max_dest_values.append(s_mi + l - 1)
        return min(min_dest_values), max(max_dest_values)


with open("day5.txt", "r") as fp:
    lines_raw = fp.readlines()

seeds = []
current_mapper: Mapper = None
mappers: List[Mapper] = []
lines_raw.append("none-to-none map:")

for line in lines_raw:
    if line.startswith("seeds:"):
        seed_numbers = line.split(":")[1].strip().split(" ")
        for seed_num_index in range(0, len(seed_numbers), 2):
            seeds.append(Seed(int(seed_numbers[seed_num_index]), int(seed_numbers[seed_num_index + 1])))
    elif line.strip().endswith("map:"):
        if current_mapper is not None:
            mappers.append(current_mapper)
        from_to_parts = line.replace(" map:", "").split("-to-")
        current_mapper = Mapper(from_to_parts[0].strip(), from_to_parts[1].strip())
    elif line.strip() == "":
        pass
    else:
        mapping_parts = line.strip().split(" ")
        current_mapper.add(RangeMap(int(mapping_parts[0]), int(mapping_parts[1]), int(mapping_parts[2])))


def find_location(start, steps):
    no_win = True
    location = 0
    i = start
    while no_win:
        current_from = "location"
        current_num = i
        story = [f'{current_from} {current_num}']
        while current_from != "seed":
            mapper = [m for m in mappers if m.to_type == current_from][0]
            current_num = mapper.map_dest(current_num)
            current_from = mapper.from_type
            story.append(f'{current_from} {current_num}')
            if current_from == "seed":
                matched_seeds = [s for s in seeds if s.num <= current_num <= s.num + s.length]
                if len(matched_seeds) > 0:
                    location = i
                    no_win = False
                    break
        i += steps

    return location


locations = []

for seed in seeds:
    current_from = "seed"
    current_num = seed.num
    story = [f'{current_from} {current_num}']
    while current_from != "location":
        mapper = [m for m in mappers if m.from_type == current_from][0]
        current_num = mapper.map_source(current_num)
        current_from = mapper.to_type
        story.append(f'{current_from} {current_num}')
        if current_from == "location":
            locations.append(current_num)


print(f'Part One: {min(locations)}')

location1 = find_location(0, 10000)
location2 = find_location(location1 - 10001, 1)

print(f"Part Two: {location2}")





