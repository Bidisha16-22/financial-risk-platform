let riskChart = null;

function calculateRisk() {
  const incomeInput = document.getElementById("income");
  const debtInput = document.getElementById("debt");
  const creditInput = document.getElementById("credit");

  const income = Number(incomeInput.value);
  const debt = Number(debtInput.value);
  const credit = Number(creditInput.value);

  if (!income || !debt || !credit) {
    alert("Please fill all fields");
    return;
  }

  fetch("/calculate-risk", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ income, debt, credit })
  })
    .then(res => res.json())
    .then(data => {
      updateRiskResult(data.risk);
      addHistoryRow(income, debt, credit, data.risk);
      updateChart(data.risk);
    })
    .catch(() => alert("Risk calculation failed"));
}

function updateRiskResult(risk) {
  const badge = document.getElementById("riskBadge");
  badge.innerText = risk;
  badge.className = "display-5 fw-bold";

  if (risk === "High") badge.style.color = "#dc3545";
  if (risk === "Medium") badge.style.color = "#ffc107";
  if (risk === "Low") badge.style.color = "#198754";
}

function resetRisk() {
  // Reset inputs
  document.getElementById("income").value = "";
  document.getElementById("debt").value = "";
  document.getElementById("credit").value = "";

  // Reset risk result
  const badge = document.getElementById("riskBadge");
  badge.innerText = "--";
  badge.style.color = "#000";

  // Reset chart
  if (riskChart) {
    riskChart.destroy();
    riskChart = null;
  }
}

function addHistoryRow(income, debt, credit, risk) {
  const tableBody = document.getElementById("historyBody");

  const row = document.createElement("tr");
  const now = new Date().toLocaleString();

  row.innerHTML = `
    <td>${now}</td>
    <td>${income}</td>
    <td>${debt}</td>
    <td>${credit}</td>
    <td>
      <span class="badge ${
        risk === "High" ? "bg-danger" :
        risk === "Medium" ? "bg-warning" :
        "bg-success"
      }">${risk}</span>
    </td>
  `;

  tableBody.prepend(row);
}

function updateChart(risk) {
  const ctx = document.getElementById("riskChart").getContext("2d");

  let counts = { High: 0, Medium: 0, Low: 0 };

  document.querySelectorAll("#historyBody tr").forEach(row => {
    const riskText = row.children[4].innerText.trim();
    if (counts[riskText] !== undefined) counts[riskText]++;
  });

  if (riskChart) riskChart.destroy();

  riskChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["High", "Medium", "Low"],
      datasets: [{
        data: [counts.High, counts.Medium, counts.Low],
        backgroundColor: ["#dc3545", "#ffc107", "#198754"]
      }]
    }
  });
}
