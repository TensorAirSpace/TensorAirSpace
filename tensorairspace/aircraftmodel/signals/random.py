import numpy as np


def full_random_signal(t0: float, dt: float, tn: float, sd: tuple, sv: tuple) -> np.ndarray:
    """
    Случайный сигнал по частоте и амплидуте

    Args:
        t0: Начальное время
        dt: Шаг дискретизации
        tn: Время сигнала
        sd: Ограничения значений по длине сигнала (min, max)
        sv: Ограничения значений по значению сигнала (min, max)

    Returns:
       Массив с случайным сигналом по частоте и амплидуте

    Пример:

    >>> signal =  full_random_signal(0,0.01,20, (-0.5, 0.5), (-0.5, 0.5))

    """
    sd_min, sd_max = sd
    sv_min, sv_max = sv
    n = int(np.floor((tn - t0) / dt) + 1)
    signal = [0 for _ in range(n)]
    step_start_time = t0
    step_duration = np.random.uniform(sd_min, sd_max)
    step_value = np.random.uniform(sv_min, sv_max)
    for i in range(n):
        t = t0 + i * dt
        signal[i] = step_value
        if t >= step_start_time + step_duration:
            step_start_time = t
            step_duration = np.random.uniform(sd_min, sd_max)
            step_value = np.random.uniform(sv_min, sv_max)

    return np.array(signal)
