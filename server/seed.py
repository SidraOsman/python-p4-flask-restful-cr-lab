#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        id=1,
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        id=2,
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )

    calathea = Plant(
        id=3,
        name="Calathea",
        image="./images/calathea.jpg",
        price=25.50,
    )

    fiddle = Plant(
        id=4,
        name="fiddle",
        image="./images/fiddle-leaf-fig.jpg",
        price= 10.99,
    )
    jade = Plant(
        id=5,
        name="Jade",
        image="./images/jade.jpg",
        price=7.50,
    )
    monstera = Plant(
        id=6,
        name="Monnstera",
        image="./images/monstera.jpg",
        price=30.05,
    )
    pilea = Plant(
        id=7,
        name="Pilea",
        image="./images/pilea.jpg",
        price=15.02,
    )
    pothos = Plant(
        id=8,
        name="Pothos",
        image="./images/pothos.jpg",
        price=17.08,
    )

    db.session.add_all([aloe, zz_plant, calathea,fiddle,jade,monstera,pilea,pothos])
    db.session.commit()
