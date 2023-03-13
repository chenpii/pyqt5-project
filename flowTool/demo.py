h = 24
V = 1500
n = 100
H_conditions = [
    [h <= 24],
    [h > 24, h <= 50],
    [h > 50],
    [h > 24]
]
V_conditions = [
    [V <= 5000],
    [V > 5000],
    [V <= 10000],
    [V > 10000],
    [V > 5000, V <= 25000],
]
data_outside = {
    '工业建筑': {
        '厂房': {
            H_conditions[0]: {
                '甲、乙、丁、戊': 10,
                '丙': {
                    V_conditions[0]: 10,
                    V_conditions[1]: 20
                }
            },
            H_conditions[1]: {
                '乙、丁、戊': 25,
                '丙': 30
            },
            H_conditions[2]: {
                '乙、丁、戊': 30,
                '丙': 40
            }
        },
        '仓库': {
            H_conditions[0]: {
                '甲、乙、丁、戊': 10,
                '丙': {
                    V_conditions[0]: 15,
                    V_conditions[1]: 25
                }
            },
            H_conditions[3]: {
                '丁、戊': 30,
                '丙': 40
            }
        }
    }
}

if all(H_conditions[0]):
    print("Yes")
