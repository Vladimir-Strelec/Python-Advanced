def render_my_screen(windows):
    login = tk.Button(windows,
                      text="Login",
                      bg="yellow",
                      bd=(5),
                      font='bold', fg='blue',
                      command=lambda: print("The login enter")).grid(row=0, column=0)
    register = tk.Button(windows,
                         text="Register",
                         bg="blue",
                         bd=(5),
                         font='bold',
                         fg='yellow',
                         command=lambda: print("The register enter")).grid(row=0, column=1)