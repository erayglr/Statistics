import random
def weighted_srs(data, n, weights, with_replacement):
  sample = []
  if with_replacement == False:
    sample.append(random.sample((data, n))
                  else:
    sample.append(random.choices((data,n)
