import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_analysis_good_quality(client: AsyncClient):
    """
    测试水质良好的场景
    """
    response = await client.post(
        "/analyze/water_quality",
        json={"ph": 7.5, "turbidity_ntu": 1.0, "dissolved_oxygen_mg_l": 8.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["assessment"] == "水质良好 (Good)"
    assert "未发现显著问题" in data["recommendations"][0]

@pytest.mark.asyncio
async def test_analysis_bad_ph(client: AsyncClient):
    """
    测试pH值异常的场景
    """
    response = await client.post(
        "/analyze/water_quality",
        json={"ph": 9.0, "turbidity_ntu": 1.0, "dissolved_oxygen_mg_l": 8.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["assessment"] == "水质异常 (Abnormal)"
    assert "pH值异常" in data["recommendations"][0]
    assert len(data["recommendations"]) == 1

@pytest.mark.asyncio
async def test_analysis_multiple_issues(client: AsyncClient):
    """
    测试多个指标异常的场景
    """
    response = await client.post(
        "/analyze/water_quality",
        json={"ph": 7.0, "turbidity_ntu": 8.0, "dissolved_oxygen_mg_l": 3.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["assessment"] == "水质异常 (Abnormal)"
    assert len(data["recommendations"]) == 2
    # Check that both relevant recommendations are present
    recommendations_text = " ".join(data["recommendations"])
    assert "浊度过高" in recommendations_text
    assert "溶解氧过低" in recommendations_text
