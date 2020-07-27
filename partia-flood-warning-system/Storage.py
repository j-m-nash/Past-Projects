x_computable = x - x[0]
poly = polyfit(dates, levels, 4)
x1 = np.linspace(x_computable[0], x_computable[-1], len(x))
x = poly(x1)