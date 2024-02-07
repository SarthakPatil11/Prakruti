// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var hr = parseInt(document.getElementById("hr").innerHTML);
var mr = parseInt(document.getElementById("mr").innerHTML);
var bl = parseInt(document.getElementById("bl").innerHTML);
var add = hr + mr + bl;
hr = (hr/add)*100;
mr = (mr/add)*100;
bl = (bl/add)*100;
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Medicine Remedies", "Home Remedies", "Blogs"],
    datasets: [{
      data: [mr, hr, bl],
      backgroundColor: ['#1cc88a', '#858796', '#e74a3b'],
      hoverBackgroundColor: ['#76d9b5', '#d4d5db', '#e9756a'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
