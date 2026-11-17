# Проверка чекпоинтов PandaPickCube

Архив содержит три чекпоинта. Основное сравнение в отчёте использует две финальные модели. Промежуточный чекпоинт нового прогона доступен для отдельной проверки.

| Обучение | Завершено итераций | Чекпоинт | Измеренный SR на стандартной сцене |
|---|---:|---|---:|
| Baseline | 1001 | [`model_1000.pt`](../experiments/baseline/model_1000.pt) | 10/10 |
| Сокращённый прогон, промежуточная модель | 101 | [`model_100.pt`](../experiments/max_iters_201/model_100.pt) | — |
| Сокращённый прогон, финальная модель | 201 | [`model_200.pt`](../experiments/max_iters_201/model_200.pt) | 0/10 |

В колонке SR у промежуточной модели пропуск, поскольку в основном сравнении оценивались финальные чекпоинты. [Контрольные суммы весов](SHA256SUMS)

## Как запустить проверку

Откройте учебный проект на коммите `70ea0fe0e039846126bd0f87f38738b710a0d515` и скопируйте в его корень папку `experiments/` из архива. Выполните команды в настроенном окружении курса. При `--seed 42 --episodes 10` скрипт использует seed от 42 до 51. `--record` сохраняет видео и позволяет запускать проверку без интерактивного окна симулятора. [Учебный проект](https://github.com/Yandex-Practicum/ap-physicalai-1/tree/70ea0fe0e039846126bd0f87f38738b710a0d515)

```bash
mkdir -p review

python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --record review/baseline.mp4

python3 inference.py --checkpoint experiments/max_iters_201/model_100.pt \
  --episodes 10 --seed 42 --record review/checkpoint_101.mp4

python3 inference.py --checkpoint experiments/max_iters_201/model_200.pt \
  --episodes 10 --seed 42 --record review/max_iters_201.mp4
```

Для проверки при другом положении куба или с шумом наблюдений используйте следующие команды. В каждом случае меняется один аспект сценария. Путь к чекпоинту можно заменить на любой из таблицы.

```bash
python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --cube_x 0.7 --cube_y 0.55 --record review/cube_far.mp4

python3 inference.py --checkpoint experiments/baseline/model_1000.pt \
  --episodes 10 --seed 42 --obs_noise 0.0275 --record review/observation_noise.mp4
```

## Контрольные результаты на изменённых сценариях

Ниже сохранённые результаты предыдущей практики для `model_1000.pt`. Контрольная сумма этой модели совпадает с baseline в архиве. Это дополнительные проверки на инференсе, поэтому они вынесены из сравнения бюджетов обучения.

| Сценарий | Захват | SR | Материалы |
|---|---:|---:|---|
| Куб сбоку, `x=0.7`, `y=0.55` | 4/10 | 2/10 | [Лог](cube_far/inference.log) · [Видео](cube_far/inference.mp4) |
| Шум наблюдений, `σ=0.0275` | 5/10 | 4/10 | [Лог](observation_noise/inference.log) · [Видео](observation_noise/inference.mp4) |

Захват засчитывается при подъёме куба выше 20 см. Для успеха куб должен оказаться ближе 5 см к цели в конце эпизода. В обоих изменённых сценариях подъём происходил чаще, чем успешная доставка.
