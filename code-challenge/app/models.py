from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

# add any models you may need. 
class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    serialize_rules = ('-powers.hero')
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    powers = db.relationship('HeroPowers', back_populates='hero')
    
    
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules = ('-heroes.power')
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    heroes = db.relationship('HeroPowers', back_populates='power')
    
class HeroPowers(db.Model, SerializerMixin):        
    __tablename__ = 'hero_powers'
    serialize_rules = ('-power.heroes', '-hero.powers')
    
    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    power = db.relationship('Power', back_populates='heroes')
    hero = db.relationship('Hero', back_populates='powers')
    