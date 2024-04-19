import { format } from "date-fns";

const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div
        className="custom-tooltip"
        style={{
          backgroundColor: "#222",
          padding: "5px",
          borderRadius: "5px",
          color: "white",
        }}
      >
        <p>{`${format(new Date(label), "MM-dd")}: $${payload[0].value.toFixed(
          2
        )}`}</p>
      </div>
    );
  }

  return null;
};

export default CustomTooltip;
