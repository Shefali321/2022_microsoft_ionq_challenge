import qsharp
import qsharp.azure
from ChineseCheckers import MeasureSpace

qsharp.azure.connect(
    resourceId="secretkey",
    location="eastus")
qsharp.azure.target("ionq.simulator")
result = qsharp.azure.execute(MeasureSpace, shots = 1, jobName="Measure space")
print("The state is", result)

# bit = MeasureSpace.simulate()
# print("The state is", bit)