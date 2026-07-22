"""Dərs məzmunu modulları (kitab: آموزش فارسی به فارسی — کتاب دوم).

Hər `lessonNN.py` modulu bir `LESSON` lüğəti ixrac edir; seed_lessons
bu siyahını avtomatik yığır.
"""
import importlib
import pkgutil

LESSONS = []
for _mod_info in pkgutil.iter_modules(__path__):
    if _mod_info.name.startswith("lesson"):
        _mod = importlib.import_module(f"{__name__}.{_mod_info.name}")
        LESSONS.append(_mod.LESSON)

LESSONS.sort(key=lambda d: d["number"])
