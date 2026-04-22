#![no_std]

use soroban_sdk::{
    contract, contractimpl, contracttype, Env, String, Address, symbol_short, Symbol
};

#[contracttype]
#[derive(Clone)]
pub struct IPRecord {
    pub id: u64,
    pub title: String,
    pub description: String,
    pub owner: Address,
}

#[contract]
pub struct IPRegistry;

#[contractimpl]
impl IPRegistry {
    const NEXT_ID: Symbol = symbol_short!("NEXT");

    pub fn create(env: Env, title: String, description: String, owner: Address) -> u64 {
        let mut id: u64 = env.storage().instance().get(&Self::NEXT_ID).unwrap_or(1);

        let record = IPRecord {
            id,
            title,
            description,
            owner,
        };

        env.storage().instance().set(&id, &record);

        id += 1;
        env.storage().instance().set(&Self::NEXT_ID, &id);

        id - 1
    }

    pub fn get(env: Env, id: u64) -> IPRecord {
        env.storage().instance().get(&id).unwrap()
    }
}