Here’s the updated list of cases, including the scenario where the **new booking’s check-in and check-out dates are identical to the existing booking**:
 (April 21, 2025, to April 25, 2025):
---

### Scenarios:

1. **Case 1: Entirely overlapping dates**  
   - **New booking request:** Check-in on April 22, 2025, and check-out on April 24, 2025.  
   - **Outcome:** Room is **unavailable** as the new booking is fully contained within the existing range.

2. **Case 2: Partial overlap (check-out falls within the range)**  
   - **New booking request:** Check-in on April 20, 2025, and check-out on April 22, 2025.  
   - **Outcome:** Room is **unavailable** as the new booking's check-out date overlaps with the existing booking's start date.

3. **Case 3: Partial overlap (check-in falls within the range)**  
   - **New booking request:** Check-in on April 24, 2025, and check-out on April 26, 2025.  
   - **Outcome:** Room is **unavailable** as the new booking's check-in date overlaps with the existing booking's end date.

4. **Case 4: Fully outside the range**  
   - **New booking request:** Check-in on April 19, 2025, and check-out on April 20, 2025.  
   - **Outcome:** Room is **available** as this booking falls entirely outside the existing range.

5. **Case 5: Spanning across the range (both check-in and check-out overlap)**  
   - **New booking request:** Check-in on April 20, 2025, and check-out on April 26, 2025.  
   - **Outcome:** Room is **unavailable** as the new booking spans across the entire existing range.

6. **Case 6: Check-out date equals the range start date**  
   - **New booking request:** Check-in on April 19, 2025, and check-out on April 21, 2025.  
   - **Outcome:** Room is **available** as the new booking's check-out date matches the existing booking’s start date (no overlap).

7. **Case 7: Check-in date equals the range end date**  
   - **New booking request:** Check-in on April 25, 2025, and check-out on April 26, 2025.  
   - **Outcome:** Room is **available** as the new booking's check-in date matches the existing booking’s end date (check-out and check-in on the same day are allowed).

8. **Case 8: Entirely after the range**  
   - **New booking request:** Check-in on April 26, 2025, and check-out on April 28, 2025.  
   - **Outcome:** Room is **available** as this booking occurs entirely after the existing range.

9. **Case 9: Check-in date equals check-out date of the existing booking**  
   - **New booking request:** Check-in on April 25, 2025, and check-out on April 28, 2025.  
   - **Outcome:** Room is **available**, as check-in on April 25 occurs after the previous guest's check-out (12 PM buffer).

10. **Case 10: Check-out date equals the check-in date of the existing booking**  
    - **New booking request:** Check-in on April 19, 2025, and check-out on April 21, 2025.  
    - **Outcome:** Room is **available**, as the new booking's check-out date matches the existing booking’s check-in date (no overlap).

11. **Case 11: New booking’s check-in and check-out dates are the same as the existing booking**  
    - **New booking request:** Check-in on April 21, 2025, and check-out on April 25, 2025.  
    - **Outcome:** Room is **unavailable** as the new booking perfectly overlaps with the existing booking (same dates).

--- 
