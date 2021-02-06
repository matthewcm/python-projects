import numpy as np
import pandas as pd
import math

corbyn_data = np.array([[13, 10], [15, 12], [14, 11], [15, 11]])
corbyn = pd.DataFrame(data=corbyn_data, columns=["Area", "Weight"])

boris_data = np.array([
    [18, 13],
    [17, 13],
    [16, 12],
    [18, 14]
])
boris = pd.DataFrame(data=boris_data, columns=["Area", "Weight"])



def column_stuff(c, column):
    print(c)

    mean = c[column].sum()/c[column].size
    print('mean: ' + str(mean))

    variance = c[column].var(ddof=False)

    print('variance: ' +str(variance))
    # for i in range(0, c['Area'].)
    # mean=O
    return {'mean':mean, 'variance':variance}

def calculate_probability( x, mean, variance ):
    exponent = math.exp(-((x - mean) ** 2 / (2 * variance)))

    return (1 / math.sqrt(2 * math.pi * variance)) * exponent


def bayesian_classifier(x, c1=corbyn, c2=boris):
    c1_area = column_stuff(c1, 'Area')
    c1_weight = column_stuff(c1, 'Weight')
    c2_area =column_stuff(c2, 'Area')
    c2_weight =column_stuff(c2, 'Weight')


    p_x1_given_c1 = (calculate_probability(x[0], c1_area['mean'], c1_area['variance']))
    p_x2_given_c1 = (calculate_probability(x[1], c1_weight['mean'], c1_weight['variance']))

    print(p_x1_given_c1)
    print(p_x2_given_c1)

    p_c1_both = p_x1_given_c1 * p_x2_given_c1

    print(p_c1_both)

    print()
    p_x1_given_c2 = (calculate_probability(x[0], c2_area['mean'], c2_area['variance']))
    p_x2_given_c2 = (calculate_probability(x[1], c2_weight['mean'], c2_weight['variance']))

    print(p_x1_given_c2)
    print(p_x2_given_c2)

    p_c2_both = p_x1_given_c2 * p_x2_given_c2
    print(p_c2_both)


    p_x_given_c1_p_c = p_c1_both * (c1.size / (c1.size + c2.size))
    p_x_given_c2_p_c = p_c2_both * (c2.size / (c1.size + c2.size))

    print()
    print(p_x_given_c1_p_c)
    print(p_x_given_c2_p_c)

    if p_x_given_c1_p_c > p_x_given_c2_p_c:
        print('CORBYN')
    else:
        print('BORIS')





def app():
    print("corbyn")
    print(corbyn)
    print("boris")
    print(boris)

    print('')
    bayesian_classifier([16,11])



if __name__ == '__main__':
    app()
