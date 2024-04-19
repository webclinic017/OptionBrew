// Utility function to check if the current time is within market hours
import { formatInTimeZone } from "date-fns-tz";

const isMarketOpen = () => {
  const now = new Date();
  const nyTimeZone = "America/New_York";

  // Get the current time in New York timezone
  const nyTime = formatInTimeZone(now, nyTimeZone, "HH:mm");

  const [hours, minutes] = nyTime.split(":").map(Number);
  const dayOfWeek = now.getUTCDay(); // Still use UTC day for consistency

  // Check if the current day is Saturday (6) or Sunday (0)
  const isWeekend = dayOfWeek === 6 || dayOfWeek === 0;

  // Check if the current time is between 9:30 AM and 4:00 PM ET
  const isOpenTime = hours > 9 || (hours === 9 && minutes >= 30);
  const isCloseTime = hours < 16 || (hours === 16 && minutes === 0);

  // Return false if it's a weekend or outside of market hours
  return !isWeekend && isOpenTime && isCloseTime;
};

export default isMarketOpen;
