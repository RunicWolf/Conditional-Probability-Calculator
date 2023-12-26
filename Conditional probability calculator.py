joint_distribution = {
    ('high', 'A', 'F_H'): 0.175, 
    ('high', '~A', 'F_H'): 0.075,
    ('normal', 'A', 'F_H'): 0.05,
    ('normal', '~A', 'F_H'): 0.2,
    ('high', 'A', '~F_H'): 0.2375,
    ('high', '~A', '~F_H'): 0.0125,
    ('normal', 'A', '~F_H'): 0.0125,
    ('normal', '~A', '~F_H'): 0.2375
}

def calculate_conditional_probability(joint_distribution, event, evidence):
    evidence_factors = evidence
    event_factors = event

    denominator_sum = 0
    numerator_sum = 0

    for key, value in joint_distribution.items():
        if all(evidence_factor in key for evidence_factor in evidence_factors):
            denominator_sum += value

    combined_factors = evidence_factors + event_factors

    for key, value in joint_distribution.items():
        if all(factor in key for factor in combined_factors):
            numerator_sum += value
            numerator_sum = round(numerator_sum, 5)

    return numerator_sum / denominator_sum if denominator_sum != 0 else 0


if __name__ == '__main__':
    event = ['high', '~F_H']
    evidence =['~A']
    prob = calculate_conditional_probability(joint_distribution, event, evidence)
    print("P({0} | {1}): {2}".format(event, evidence, prob))
