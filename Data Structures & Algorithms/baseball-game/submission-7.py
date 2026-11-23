class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        running_sum = 0
        for operation in operations:
            match operation:
                case "+":
                    records.append(records[-1] + records[-2])
                    running_sum += records[-1]
                case "D":
                    records.append(records[-1] * 2)
                    running_sum += records[-1]
                case "C":
                    running_sum -= records.pop()
                case _:
                    records.append(int(operation))
                    running_sum += records[-1]
        return running_sum