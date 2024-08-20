from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self, cable: Cable, times: int):
        # cable length must be between 2 and 1024 inclusive
        if not (2 <= cable.length <= 1024):
            raise ValueError("Cable length must be between 2 and 1024 inclusive")

        # times must be between 1 and 64 inclusive
        if not (1 <= times <= 64):
            raise ValueError("Times must be between 1 and 64 inclusive")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable=cable, times=times)

        # minimum pieces is the number of splits + 1
        min_pieces = times + 1

        longest_length = cable.length // min_pieces

        if longest_length < 1:
            raise ValueError("Cable length must be greater than or equal to 1")

        # check if there are any remainder cable
        # if there are remainder, cut the remainder using the longest length
        # assume that the remainder could be cut into multiple pieces of the longest length
        remainder_length = cable.length % min_pieces
        while remainder_length > longest_length:
            min_pieces += 1
            remainder_length -= longest_length

        # calculate total pieces
        # if there are remainder, add 1 to the total pieces
        total_pieces = min_pieces + 1 if remainder_length > 0 else 0

        id_alignment = len(str(total_pieces))

        # for each pieces, create a cable with the longest length
        cables = [
            Cable(
                length=longest_length,
                name=cable.name + "-" + str(i).rjust(id_alignment, "0"),
            )
            for i in range(min_pieces)
        ]

        # if there are remainder, create a cable with the remainder length
        if remainder_length > 0:
            cables.append(
                Cable(
                    length=remainder_length,
                    name=cable.name + "-" + str(min_pieces).rjust(id_alignment, "0"),
                )
            )

        return cables
