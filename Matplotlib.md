
## Main Code
```python
import matplotlib
import matplotlib.pyplot as plt
fig,axes = plt.subplots()

# the above commands set the canvas 
# for plotting the graphs
```
Axes is an object on which the x-axis variable is plotted. This only sets the space through the four main parameters
1. Left Margin
2. Bottom Margin
3. Width
4. Height
All the above are set between 0 and 1. Note that Left + Width, if exceeding 1 means that the visual will go out of view, same goes for Bottom + Height.
> The axes design is set through default settings once the above command is called and need not be changed

#### Focus on running the data transformation operations in Excel, PowerPivot

Running the dataplots with specific legend requirements can be done using the `for` loop based on the legend column
The example is available [here](https://gist.github.com/nilotpalc/3a440e56b54acbc4bed8e2c0760769b9)

The input to various plots can be in the form of a list or array. Hence, we can use commands like `df[col].unique()` to plot the x-axis while using `df[col]` to plot the y-axis. Also, note we can also use conditional selection to select the y-axis `df[df[col] > a][col3]`.
Point to rem

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNjQyMDY2OTIsNTY4ODQ2Nzk4XX0=
-->