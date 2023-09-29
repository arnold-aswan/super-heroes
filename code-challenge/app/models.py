from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# add any models you may need. 
class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heros'
    serialize_rules = ('-powers.hero')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    powers = db.relationship('HeroPower', back_populates='hero')
   
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules = ('-heros.power')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    heros = db.relationship('HeroPower', back_populates='power')
    
class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    serialize_rules = ('-hero.powers', '-power.heros')
    
    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))  
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))   
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())   
    
    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heros')

    