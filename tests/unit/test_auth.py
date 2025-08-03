import pytest
from app.utils.auth import verify_password, get_password_hash


def test_password_hashing():
    """Test password hashing and verification"""
    password = "test_password"
    hashed = get_password_hash(password)
    
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrong_password", hashed)


def test_password_hash_is_different_each_time():
    """Test that password hashing produces different results"""
    password = "test_password"
    hash1 = get_password_hash(password)
    hash2 = get_password_hash(password)
    
    assert hash1 != hash2
    assert verify_password(password, hash1)
    assert verify_password(password, hash2)