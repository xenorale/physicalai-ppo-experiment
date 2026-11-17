# Проверка чекпоинтов PandaPickCube

В архиве три чекпоинта. В отчёте я сравнил две финальные модели. Третий чекпоинт сохранил в середине короткого прогона, его можно проверить отдельно.

| Прогон | Итераций | Чекпоинт | Успешных попыток на обычной сцене |
|---|---:|---|---:|
| Baseline | 1001 | [`model_1000.pt`](../experiments/baseline/model_1000.pt) | 10/10 |
| Короткий прогон, промежуточная модель | 101 | [`model_100.pt`](../experiments/max_iters_201/model_100.pt) | Не проверял |
| Короткий прогон, финальная модель | 201 | [`model_200.pt`](../experiments/max_iters_201/model_200.pt) | 0/10 |

[Контрольные суммы весов](SHA256SUMS)

## Как запустить проверку

Возьмите учебный проект по ссылке ниже и скопируйте в него папку `experiments/` из архива. Запустите команды в окружении курса. В каждой проверке будет 10 попыток с seed от 42 до 51. Флаг `--record` сохраняет видео без открытия окна симулятора. [Учебный проект](https://github.com/Yandex-Practicum/ap-physicalai-1/tree/70ea0fe0e039846126bd0f87f38738b710a0d515)

```bash
mkdir -p review

python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --record review/baseline.mp4

python3 inference.py --checkpoint experiments/max_iters_201/model_100.pt \
  --episodes 10 --seed 42 --record review/checkpoint_101.mp4

python3 inference.py --checkpoint experiments/max_iters_201/model_200.pt \
  --episodes 10 --seed 42 --record review/max_iters_201.mp4
```

Первая команда ниже сдвигает куб, вторая добавляет шум к данным, которые получает модель. В обеих командах можно подставить любой чекпоинт из таблицы.

```bash
python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --cube_x 0.7 --cube_y 0.55 --record review/cube_far.mp4

python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --obs_noise 0.0275 --record review/observation_noise.mp4
```

## Что получилось со смещённым кубом и шумом

Эти результаты остались с предыдущей практики. Я проверял тот же `model_1000.pt`, который лежит в архиве. В обоих случаях использовал готовую модель.

| Сценарий | Захват | SR | Материалы |
|---|---:|---:|---|
| Куб сбоку, `x=0.7`, `y=0.55` | 4/10 | 2/10 | [Лог](cube_far/inference.log) · [Видео](cube_far/inference.mp4) |
| Шум наблюдений, `σ=0.0275` | 5/10 | 4/10 | [Лог](observation_noise/inference.log) · [Видео](observation_noise/inference.mp4) |

Захват засчитывается при подъёме куба выше 20 см. Для успеха куб должен оказаться ближе 5 см к цели в конце эпизода. В обоих изменённых сценариях подъём происходил чаще, чем успешная доставка.
