class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            match operation:
                case "+":
                    records.append(records[-1] + records[-2])
                case "D":
                    records.append(records[-1] * 2)
                case "C":
                    records.pop()
                case _:
                    records.append(int(operation))
        return sum(records)