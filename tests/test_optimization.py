import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_optimize_high_level(client: AsyncClient):
    """
    测试高水位情况下的调度优化
    """
    response = await client.post(
        "/optimize/reservoir_dispatch",
        json={
            "reservoir_level_m": 105,
            "downstream_demand_m3_s": 50,
            "inflow_m3_s": 60
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "增加下泄流量" in data["message"]
    # outflow should be inflow * 1.2 = 72
    assert data["outflow_m3_s"] == 72.0

@pytest.mark.asyncio
async def test_optimize_low_level(client: AsyncClient):
    """
    测试低水位情况下的调度优化
    """
    response = await client.post(
        "/optimize/reservoir_dispatch",
        json={
            "reservoir_level_m": 65,
            "downstream_demand_m3_s": 50,
            "inflow_m3_s": 40
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "减少下泄流量" in data["message"]
    # outflow should be inflow * 0.8 = 32
    assert data["outflow_m3_s"] == 32.0

@pytest.mark.asyncio
async def test_optimize_normal_level(client: AsyncClient):
    """
    测试正常水位情况下的调度优化
    """
    response = await client.post(
        "/optimize/reservoir_dispatch",
        json={
            "reservoir_level_m": 85,
            "downstream_demand_m3_s": 55,
            "inflow_m3_s": 50
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "调度方案正常" in data["message"]
    # outflow should be downstream_demand = 55
    assert data["outflow_m3_s"] == 55.0
