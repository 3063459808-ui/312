import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_predict_high_risk(client: AsyncClient):
    """
    测试高洪水风险场景
    """
    response = await client.post(
        "/predict/flood_drought",
        json={"rainfall_mm": 60, "river_level_m": 3.5}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "高 (High)"
    assert "高洪水风险" in data["message"]

@pytest.mark.asyncio
async def test_predict_drought_risk(client: AsyncClient):
    """
    测试干旱风险场景
    """
    response = await client.post(
        "/predict/flood_drought",
        json={"rainfall_mm": 2, "river_level_m": 0.4}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "中 (Medium)"
    assert "干旱风险" in data["message"]

@pytest.mark.asyncio
async def test_predict_low_risk(client: AsyncClient):
    """
    测试低风险场景
    """
    response = await client.post(
        "/predict/flood_drought",
        json={"rainfall_mm": 20, "river_level_m": 1.5}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "低 (Low)"
    assert "稳定" in data["message"]

@pytest.mark.asyncio
async def test_predict_invalid_input(client: AsyncClient):
    """
    测试无效输入（例如，缺少字段）
    FastAPI/Pydantic应该返回422 Unprocessable Entity
    """
    response = await client.post(
        "/predict/flood_drought",
        json={"rainfall_mm": 60} # river_level_m is missing
    )
    assert response.status_code == 422
