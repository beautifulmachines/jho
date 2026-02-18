"Tests for JHO mission model"
import pytest


def test_mission_build():
    "Mission model instantiates without error"
    from model.jho import Mission

    m = Mission()
    assert len(m.vks) > 100


def test_mission_solve():
    "Mission model solves and produces physically reasonable MTOW"
    from model.jho import Mission

    model = Mission()
    model.substitutions[model.JHO.emp.vtail.Vv] = 0.04
    model.substitutions[model.loiter["t"]] = 6
    model.cost = model["MTOW"]
    sol = model.localsolve(verbosity=0)
    mtow = sol["MTOW"].magnitude
    # JHO as-built was ~150 lbf; reasonable range 80-300 lbf
    assert 80 < mtow < 300, f"MTOW {mtow} lbf out of reasonable range"


def test_mission_max_endurance():
    "Original test(): maximize endurance (minimize 1/t)"
    from model.jho import Mission

    model = Mission()
    model.substitutions[model.JHO.emp.vtail.Vv] = 0.04
    model.cost = 1 / model.loiter["t"]
    sol = model.localsolve(verbosity=0)
    endurance_days = sol[model.loiter["t"]].magnitude
    assert endurance_days > 0, "Endurance should be positive"
