# cool Hecker prgram trust
hecker = input("Are you a hecker? ").strip().lower()
can_heck = input("Can you heck? ").strip().lower()

# checks if hecker is cool

if hecker in ("yes", "y") and can_heck in ("yes", "y"):
    print("Enter the cool hecker group")
else:
    print("You’re not hecker enough to join the cool hecker group")
