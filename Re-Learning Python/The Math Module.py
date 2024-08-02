import math

# Basic arithmetic operations (addition, subtraction, multiplication, division)
# Trigonometric functions (sine, cosine, tangent, and their inverses)
# Hyperbolic functions (sinh, cosh, tanh, and their inverses)
# Exponential and logarithmic functions
# Special functions (gamma, error function, etc.)
# Angle conversions (degrees to radians and vice versa)
# Floating point operations (checking for infinity, NaN, etc.)


# Calculate the square root of a given number
number = 16
sqrt_result = math.sqrt(number)
print(f"The square root of {number} is {sqrt_result}")  # Output: 4.0

# Calculate a number raised to the power of another number
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}")  # Output: 8.0

# Calculate the sine of an angle in degrees (converted to radians)
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
sine_result = math.sin(angle_radians)
print(f"The sine of {angle_degrees} degrees (or {angle_radians} radians) is {sine_result}")  # Output: 1.0

# Calculate the cosine of an angle in degrees (converted to radians)
angle_degrees = 0
angle_radians = math.radians(angle_degrees)
cosine_result = math.cos(angle_radians)
print(f"The cosine of {angle_degrees} degrees (or {angle_radians} radians) is {cosine_result}")  # Output: 1.0

# Calculate the tangent of an angle in degrees (converted to radians)
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
tangent_result = math.tan(angle_radians)
print(f"The tangent of {angle_degrees} degrees (or {angle_radians} radians) is {tangent_result}")  # Output: 1.0

# Calculate the natural logarithm of a given number
number = 10
log_result = math.log(number)
print(f"The natural logarithm (base e) of {number} is {log_result}")  # Output: 2.302585092994046

# Calculate the base-10 logarithm of a given number
number = 1000
log10_result = math.log10(number)
print(f"The base-10 logarithm of {number} is {log10_result}")  # Output: 3.0

# Print the value of Pi
print(f"The value of Pi (π) is {math.pi}")  # Output: 3.141592653589793

# Print the value of Euler's number
print(f"The value of Euler's number (e) is {math.e}")  # Output: 2.718281828459045


# Calculate the exponential of a number (e^x)
number = 2
exp_result = math.exp(number)
print(f"The exponential of {number} (e^{number}) is {exp_result}")  # Output: 7.3890560989306495

# Calculate the natural logarithm of 1 plus a number
number = 1
log1p_result = math.log1p(number)
print(f"The natural logarithm of 1 plus {number} is {log1p_result}")  # Output: 0.6931471805599453

# Calculate the hyperbolic sine of a number
number = 1
sinh_result = math.sinh(number)
print(f"The hyperbolic sine of {number} is {sinh_result}")  # Output: 1.1752011936438014

# Calculate the hyperbolic cosine of a number
number = 1
cosh_result = math.cosh(number)
print(f"The hyperbolic cosine of {number} is {cosh_result}")  # Output: 1.5430806348152437

# Calculate the hyperbolic tangent of a number
number = 1
tanh_result = math.tanh(number)
print(f"The hyperbolic tangent of {number} is {tanh_result}")  # Output: 0.7615941559557649

# Convert degrees to radians
degrees = 180
radians_result = math.radians(degrees)
print(f"{degrees} degrees is {radians_result} radians")  # Output: 3.141592653589793

# Convert radians to degrees
radians = math.pi
degrees_result = math.degrees(radians)
print(f"{radians} radians is {degrees_result} degrees")  # Output: 180.0

# Calculate the arc sine of a number
number = 1
asin_result = math.asin(number)
print(f"The arc sine of {number} is {asin_result} radians")  # Output: 1.5707963267948966

# Calculate the arc cosine of a number
number = 1
acos_result = math.acos(number)
print(f"The arc cosine of {number} is {acos_result} radians")  # Output: 0.0

# Calculate the arc tangent of a number
number = 1
atan_result = math.atan(number)
print(f"The arc tangent of {number} is {atan_result} radians")  # Output: 0.7853981633974483

# Calculate the arc sine of a number
number = 1
asin_result = math.asin(number)
print(f"The arc sine of {number} is {asin_result} radians")  # Output: 1.5707963267948966

# Calculate the arc cosine of a number
number = 1
acos_result = math.acos(number)
print(f"The arc cosine of {number} is {acos_result} radians")  # Output: 0.0

# Calculate the arc tangent of a number
number = 1
atan_result = math.atan(number)
print(f"The arc tangent of {number} is {atan_result} radians")  # Output: 0.7853981633974483

# Calculate the error function (erf) of a number
number = 1
erf_result = math.erf(number)
print(f"The error function of {number} is {erf_result}")  # Output: 0.8427007929497148

# Calculate the complementary error function (erfc) of a number
number = 1
erfc_result = math.erfc(number)
print(f"The complementary error function of {number} is {erfc_result}")  # Output: 0.15729920705028513

# Calculate the gamma function of a number
number = 5
gamma_result = math.gamma(number)
print(f"The gamma function of {number} is {gamma_result}")  # Output: 24.0

# Calculate the natural logarithm of the absolute value of the gamma function of a number
number = 5
lgamma_result = math.lgamma(number)
print(f"The natural logarithm of the absolute value of the gamma function of {number} is {lgamma_result}")  # Output: 3.178053830347945

# Check if a number is finite
number = math.pi
is_finite = math.isfinite(number)
print(f"Is {number} finite? {is_finite}")  # Output: True

# Check if a number is infinite
number = float('inf')
is_infinite = math.isinf(number)
print(f"Is {number} infinite? {is_infinite}")  # Output: True

# Check if a number is NaN (Not a Number)
number = float('nan')
is_nan = math.isnan(number)
print(f"Is {number} NaN? {is_nan}")  # Output: True

