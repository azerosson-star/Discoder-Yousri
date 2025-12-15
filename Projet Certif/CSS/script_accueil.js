/**
 * INTERACTIVE PIE CHART WITH 6+ CLICKABLE SECTIONS
 * ================================================
 * This script creates an interactive pie chart using Chart.js that displays
 * student performance or subject distribution data. Each slice is clickable
 * and displays detailed information. The chart includes smart label positioning
 * with leader lines for small slices to avoid cluttering.
 */

// Get the canvas element context for drawing the Chart.js pie chart
// The '2d' context allows us to draw 2D graphics on the canvas
const ctx = document.getElementById('pieChart').getContext('2d');

// Reference to the div that will display information when a slice is clicked
const infoDiv = document.getElementById('info');

/**
 * DATA STRUCTURE: Array of objects containing information for each pie slice
 * - label: Name of the subject/category
 * - value: Numeric value determining the slice size
 * - color: Hex color code for visual identification
 * 
 * The pie chart will automatically calculate percentages based on these values.
 * Each value is proportional to its slice size in the pie.
 */
const data = [
    { label: 'Math', value: 2, color: '#FF6384' },        // Red: 2 units
    { label: 'French', value: 20, color: '#36A2EB' },     // Blue: 20 units (largest)
    { label: 'English', value: 15, color: '#FFCE56' },    // Yellow: 15 units
    { label: 'History', value: 1, color: '#4BC0C0' },     // Teal: 1 unit (smallest)
    { label: 'Geography', value: 12, color: '#9966FF' },  // Purple: 12 units
    { label: 'Biology', value: 10, color: '#FF9F40' },    // Orange: 10 units
    { label: 'Physics', value: 8, color: '#C9CBCF' }      // Gray: 8 units
];

/**
 * EXTRACT DATA FOR CHART.JS
 * These arrays transform the data structure into a format Chart.js expects:
 * - labels: Category names to identify each slice
 * - values: The actual numbers that determine slice sizes
 * - colors: Visual colors for each slice in the pie
 */
const labels = data.map(d => d.label);      // Extract all subject names
const values = data.map(d => d.value);      // Extract all numeric values
const colors = data.map(d => d.color);      // Extract all color codes


/**
 * CUSTOM LABEL PLUGIN FOR CHART.JS
 * =================================
 * This plugin draws labels directly on the pie chart slices with intelligent
 * positioning. Small slices (< 8%) get leader lines pointing to external labels
 * to avoid overlapping with the pie itself. Larger slices get labels placed
 * directly on the slice.
 * 
 * Why use a plugin? Chart.js doesn't natively support this level of label
 * customization, so we extend it with a custom plugin.
 */
const labelPlugin = {
    /**
     * afterDatasetsDraw: Fires AFTER Chart.js draws all the data
     * This is the perfect time to add our custom labels on top
     */
    afterDatasetsDraw(chart) {
        const { ctx, data, chartArea } = chart;
        
        // CALCULATE PIE DIMENSIONS
        // Find the center point of the pie chart
        const centerX = (chartArea.left + chartArea.right) / 2;
        const centerY = (chartArea.top + chartArea.bottom) / 2;
        
        // Calculate the radius (distance from center to edge)
        // Use the smaller dimension to ensure the pie fits within the chart area
        const radius = Math.min(chartArea.right - centerX, centerY - chartArea.top);

        // Process each dataset (in our case, just the pie data)
        data.datasets.forEach((dataset) => {
            // Start angle at -90 degrees (top of the pie)
            let currentAngle = -Math.PI / 2;
            
            // Calculate total sum of all values for percentage calculations
            const total = dataset.data.reduce((a, b) => a + b, 0);

            /**
             * FOR EACH SLICE IN THE PIE
             * Process slices one by one and draw labels for each
             */
            dataset.data.forEach((value, index) => {
                // Calculate the angle that this slice occupies
                // Formula: (value / total) * 360 degrees = (value / total) * 2π radians
                const sliceAngle = (value / total) * 2 * Math.PI;
                
                // Calculate the middle angle of this slice (where label should be placed)
                const midAngle = currentAngle + sliceAngle / 2;
                
                // Determine if this is a "small slice" that needs a leader line
                // Slices smaller than 8% of the total are considered small
                // This prevents labels from overlapping the pie
                const isSmallSlice = (value / total) * 100 < 8;

                // POSITION LABEL ON THE SLICE
                // Different distance for small vs large slices
                // Small slices: label at 70% of radius (more inward)
                // Large slices: label at 65% of radius
                const labelRadius = isSmallSlice ? radius * 0.7 : radius * 0.65;
                
                // Convert polar coordinates (angle, distance) to Cartesian (x, y)
                // This positions where the label will be placed
                const labelX = centerX + Math.cos(midAngle) * labelRadius;
                const labelY = centerY + Math.sin(midAngle) * labelRadius;

                // Get the label text (subject name)
                const label = data.labels[index];
                const text = `${label}`;

                // STYLE THE TEXT
                ctx.fillStyle = '#000';              // Black text
                ctx.font = 'bold 12px Arial';        // Bold 12px font
                ctx.textAlign = 'center';            // Center horizontally
                ctx.textBaseline = 'middle';         // Center vertically

                if (isSmallSlice) {
                    /**
                     * LEADER LINE FOR SMALL SLICES
                     * ============================
                     * For small slices, we draw:
                     * 1. A radial line from the slice to an "elbow" point
                     * 2. A horizontal line extending from the elbow
                     * 3. The label centered on the horizontal line
                     * 
                     * This prevents cluttered text and makes small slices readable
                     */
                    
                    // Starting point: where the leader line begins (on the pie)
                    const innerX = centerX + Math.cos(midAngle) * radius * 0.65;
                    const innerY = centerY + Math.sin(midAngle) * radius * 0.65;

                    // Elbow point: slightly outside the pie where line bends
                    // Located at 103% of radius for a subtle offset
                    const elbowRadius = radius * 1.03;
                    const elbowX = centerX + Math.cos(midAngle) * elbowRadius;
                    const elbowY = centerY + Math.sin(midAngle) * elbowRadius;

                    // HORIZONTAL SEGMENT CALCULATION
                    // Determine length and direction of the horizontal line
                    const preferredHorizontalLen = 48; // 48 pixels for the horizontal part
                    
                    // Direction: +1 for right side (cos >= 0), -1 for left side (cos < 0)
                    // This ensures labels point outward, not inward
                    const side = Math.cos(midAngle) >= 0 ? 1 : -1;

                    // Calculate where the horizontal line ends
                    // But first, clamp it to stay within chart boundaries
                    const maxRight = chartArea.right - 6;    // 6px margin from right edge
                    const minLeft = chartArea.left + 6;      // 6px margin from left edge
                    
                    let horizEndX = elbowX + side * preferredHorizontalLen;
                    const horizEndY = elbowY;

                    // If the horizontal line would go outside the chart, clamp it
                    if (horizEndX > maxRight) {
                        horizEndX = maxRight;
                    } else if (horizEndX < minLeft) {
                        horizEndX = minLeft;
                    }

                    /**
                     * DRAW THE LEADER LINES
                     * Two connected line segments: radial + horizontal
                     */
                    ctx.strokeStyle = '#666';       // Gray color for leader lines
                    ctx.lineWidth = 1;              // Thin lines
                    ctx.beginPath();
                    ctx.moveTo(innerX, innerY);     // Start from the slice
                    ctx.lineTo(elbowX, elbowY);     // Draw to the elbow
                    ctx.lineTo(horizEndX, horizEndY); // Draw horizontal segment
                    ctx.stroke();

                    /**
                     * DRAW LABEL TEXT ON HORIZONTAL SEGMENT
                     * Place the label centered on the horizontal line
                     */
                    ctx.fillStyle = '#000';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'bottom';    // Align text above the line
                    
                    // Calculate center point of horizontal segment for label placement
                    const midHorizX = (elbowX + horizEndX) / 2;
                    
                    // Draw the text at the midpoint of the horizontal line
                    ctx.fillText(text, midHorizX, horizEndY);
                    
                } else {
                    /**
                     * DIRECT LABEL FOR LARGE SLICES
                     * For slices >= 8%, just draw the label directly on the slice
                     * No leader lines needed as there's enough space
                     */
                    ctx.fillText(text, labelX, (labelY));
                }

                // Update the current angle for the next slice
                currentAngle += sliceAngle;
            });
        });
    }
};


/**
 * CREATE AND CONFIGURE THE PIE CHART
 * ==================================
 * Instantiate a new Chart.js pie chart with all the data and configuration
 */
const pieChart = new Chart(ctx, {
    type: 'pie',  // Pie chart type
    
    /**
     * DATA CONFIGURATION
     * Bind our extracted labels and values to the chart
     */
    data: {
        labels: labels,  // Subject names for each slice
        datasets: [{
            data: values,                           // Numeric values determining slice sizes
            backgroundColor: colors,                // Colors for each slice
            borderColor: '#fff',                    // White border between slices
            borderWidth: 2,                         // 2px border thickness
            hoverOffset: 10                         // Slice moves 10px when hovered (visual feedback)
        }]
    },
    
    /**
     * CHART OPTIONS & BEHAVIOR
     * Configure how the chart displays and behaves
     */
    options: {
        responsive: true,           // Chart resizes with window
        maintainAspectRatio: true,  // Keep circular shape (don't squash)
        
        /**
         * PADDING/MARGINS
         * Extra space around the chart to prevent labels from touching edges
         */
        layout: {
            padding: {
                left: 20,
                right: 20,
                top: 10,
                bottom: 10
            }
        },
        
        /**
         * PLUGINS CONFIGURATION
         * Customize tooltips, legends, and custom plugins
         */
        plugins: {
            legend: {
                display: false  // Hide the default legend (we use custom labels instead)
            },
            
            /**
             * TOOLTIP CONFIGURATION
             * The info box that appears when hovering over slices
             */
            tooltip: {
                callbacks: {
                    /**
                     * CUSTOM TOOLTIP TEXT
                     * Instead of default tooltip, show: "Name: value (percentage%)"
                     * Example: "French: 20 (34.5%)"
                     */
                    label: function (context) {
                        const label = context.label || '';
                        const value = context.parsed || 0;
                        
                        // Calculate percentage of total
                        const total = context.dataset.data.reduce((a, b) => a + b, 0);
                        const percentage = ((value / total) * 100).toFixed(1); // Round to 1 decimal
                        
                        // Return formatted tooltip text
                        return `${label}: ${value} (${percentage}%)`;
                    }
                }
            },
            
            labelPlugin: true  // Enable our custom label plugin
        },
        
        /**
         * CLICK HANDLER
         * When user clicks a pie slice, display its information
         */
        onClick: (event, elements) => {
            // Check if click was on a slice (not empty space)
            if (elements.length > 0) {
                // Get the index of the clicked slice
                const index = elements[0].index;
                
                // Get the data for that slice
                const selectedData = data[index];
                
                // Update the info div with the slice details
                // HTML: bold subject name, then value on next line
                infoDiv.innerHTML = `<strong>${selectedData.label}</strong><br>Valeur: ${selectedData.value}`;
                
                // Color the text to match the slice color
                infoDiv.style.color = selectedData.color;
            }
        }
    },
    
    /**
     * REGISTER CUSTOM PLUGIN
     * Tell Chart.js to use our custom label plugin
     */
    plugins: [labelPlugin]
});