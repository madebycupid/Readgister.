from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql, os

from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/profile_p/"
app.secret_key = "newjeans" 



connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "spinadirosula111",
    database = "readgister",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connection.cursor()

@app.route("/")
def landing_page():
    sql = "SELECT * FROM staff_acc"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("landing_page.html", std=result)

@app.route("/booklist", methods=["GET"])
def booklist():
    
    search = request.args.get("search", "")
    course = request.args.get("course", "")

    sql = "SELECT * FROM book_list WHERE 1=1"
    params = []

    if search:
        sql += " AND (title_book LIKE %s OR author_book LIKE %s)"
        params.extend([f"%{search}%", f"%{search}%"])

    if course and course != "ALL":
        sql += " AND course_book = %s"
        params.append(course)

    sql += " ORDER BY title_book ASC"

    cursor.execute(sql, params)
    books = cursor.fetchall()

    return render_template("booklist.html", books=books, search=search, course=course)

@app.route("/book_details")
def book_details():
    
    book_id = request.args.get("book_id")
    sql = "SELECT * FROM book_list WHERE id_book=%s"
    cursor.execute(sql, (book_id,))
    book = cursor.fetchone()

    return render_template("book_details.html", book=book)


# ====================== admin page ======================
@app.route("/admin_home_page")
def admin_home_page():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    admin_id = session["admin_id"]
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()

    return render_template("admin_home_page.html", admin=admin)


@app.route("/admin_profile", methods=["GET", "POST"])
def admin_profile():
    admin_id = session["admin_id"]

    if "admin_id" not in session:
        return redirect(url_for("admin_login"))

    if request.method == "POST":
        admin_photo = request.files.get('photo_admin')
        admin_name = request.form.get('name_admin')
        admin_email = request.form.get('email_admin')
        admin_phone = request.form.get('phone_admin')
        admin_pass = request.form.get('pass_admin')

        if admin_photo and admin_photo.filename != "":
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], admin_photo.filename)
            admin_photo.save(photo_path)

            admin_pic = "profile_p/" + admin_photo.filename

            sql = "UPDATE admin_acc SET profile_admin=%s, name_admin=%s, email_admin=%s, phone_admin=%s, pass_admin=%s WHERE id_admin=%s"
            cursor.execute(sql, (admin_pic, admin_name, admin_email, admin_phone, admin_pass, admin_id,))

        else:
            sql = "UPDATE admin_acc SET name_admin=%s, email_admin=%s, phone_admin=%s, pass_admin=%s WHERE id_admin=%s"
            cursor.execute(sql, (admin_name, admin_email, admin_phone, admin_pass, admin_id,))
        
        connection.commit()

        flash("Successfully updated!")
        return redirect(url_for("admin_profile"))

    sql = "SELECT * FROM admin_acc WHERE id_admin=%s"
    cursor.execute(sql, (admin_id,))
    admin = cursor.fetchone()

    return render_template("admin_profile.html", admin=admin)



#admin log-in
@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/admin_login_process", methods=['POST'])
def admin_login_process():
    admin_user = request.form.get("user_admin")
    admin_pass = request.form.get("pass_admin")

    sql = "SELECT * FROM admin_acc WHERE user_admin=%s AND pass_admin=%s"
    cursor.execute(sql, (admin_user, admin_pass))
    account_found = cursor.fetchone()

    if account_found:
        session["admin_id"] = account_found["id_admin"]
        return redirect(url_for("admin_home_page"))
    else:
        flash("Wrong Username or Password")
        return redirect(url_for("admin_login"))
    
@app.route("/admin_logout")
def admin_logout():
    session.pop("admin_id")
    flash("You have been logged out.")
    return redirect(url_for("admin_login"))
    

#admin dashboard
@app.route("/admin_dashboard_books", methods=["GET", "POST"])
def admin_dashboard_books():
    admin_id = session["admin_id"]

    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    if request.method == "POST":
        title = request.form.get("title_book")
        author = request.form.get("author_book")
        year = request.form.get("year_book")
        desc = request.form.get("desc_book")
        course = request.form.get("course_book")
        quantity = request.form.get("quantity_book")
        cover = request.files.get("cover_book")

        if cover and cover.filename != "":
            cover_path = os.path.join(app.config['UPLOAD_FOLDER'], cover.filename)
            cover.save(cover_path)

            book_cover = "profile_p/" + cover.filename
        else:
            book_cover = "profile_p/cover_default.jpg"

        sql = "INSERT INTO book_list (title_book, author_book, year_book, desc_book, course_book, quantity_book, photo_book, status_book) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
        cursor.execute(sql, (title, author, year, desc, course, quantity, book_cover, "available"))

        connection.commit()

        flash("Book added successfully.")
        return redirect(url_for("booklist_admin"))
    
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()

    return render_template("admin_dashboard_books.html", admin=admin)


@app.route("/booklist_admin", methods=["GET"])
def booklist_admin():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    search = request.args.get("search", "")
    course = request.args.get("course", "")

    sql = "SELECT * FROM book_list WHERE 1=1"
    params = []

    if search:
        sql += " AND (title_book LIKE %s OR author_book LIKE %s)"
        params.extend([f"%{search}%", f"%{search}%"])

    if course and course != "ALL":
        sql += " AND course_book = %s"
        params.append(course)

    sql += " ORDER BY title_book ASC"

    cursor.execute(sql, params)
    books = cursor.fetchall()

    admin_id = session["admin_id"]
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()

    return render_template("booklist_admin.html", books=books, search=search, course=course, admin=admin)

@app.route("/book_details_admin")
def book_details_admin():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    book_id = request.args.get("book_id")
    sql = "SELECT * FROM book_list WHERE id_book=%s"
    cursor.execute(sql, (book_id,))
    book = cursor.fetchone()
    
    admin_id = session["admin_id"]
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()

    return render_template("book_details_admin.html", admin=admin, book=book)

@app.route("/book_details_admin_update", methods=["GET", "POST"])
def book_details_admin_update():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    admin_id = session["admin_id"]
    book_id = request.args.get("book_id")

    sql = "SELECT * FROM book_list WHERE id_book=%s"
    cursor.execute(sql, (book_id,))
    book = cursor.fetchone()

    if request.method == "POST":
        title = request.form.get("title_book")
        author = request.form.get("author_book")
        year = request.form.get("year_book")
        desc = request.form.get("desc_book")
        course = request.form.get("course_book")
        quantity = request.form.get("quantity_book")
        cover = request.files.get("cover_book")

        if cover and cover.filename != "":
            cover_path = os.path.join(app.config['UPLOAD_FOLDER'], cover.filename)
            cover.save(cover_path)
            book_cover = "profile_p/" + cover.filename
        else:
            book_cover = book["photo_book"]

        sql = "UPDATE book_list SET title_book=%s, author_book=%s, year_book=%s, desc_book=%s, course_book=%s, quantity_book=%s, photo_book=%s WHERE id_book=%s"

        cursor.execute(sql, (title, author, year, desc, course, quantity, book_cover, book_id))
        connection.commit()

        flash("Book updated successfully.")
        return redirect(url_for("booklist_admin"))
    
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()

    return render_template("book_details_admin_update.html", admin=admin, book=book)

@app.route("/book_details_admin_delete", methods=["POST"])
def book_details_admin_delete():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    book_id = request.form.get("book_id")

    sql = "DELETE FROM book_list WHERE id_book=%s"
    cursor.execute(sql, (book_id,))
    connection.commit()

    flash("Book deleted successfully.")
    return redirect(url_for("booklist_admin"))




@app.route("/admin_dashboard_staff")
def admin_dashboard_staff():
    if "admin_id" not in session:
        return render_template("landing_page.html")
    
    admin_id = session["admin_id"]
    cursor.execute("SELECT * FROM admin_acc WHERE id_admin=%s", (admin_id,))
    admin = cursor.fetchone()
    
    sql = "SELECT * FROM staff_acc"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("admin_dashboard_staff.html", std=result, admin=admin)

@app.route("/admin_dashboard_staff_approval", methods=['POST'])
def admin_dashboard_staff_approval():
    staff_id = request.form.get("staff_id")
    sql = "UPDATE staff_acc SET status_staff='approved' WHERE id_staff=%s"
    cursor.execute(sql, (staff_id,))
    connection.commit()

    flash("Staff has been approved!")
    return redirect(url_for("admin_dashboard_staff"))

@app.route("/admin_dashboard_staff_reject", methods=['POST'])
def admin_dashboard_staff_reject():
    staff_id = request.form.get("staff_id")
    sql = "UPDATE staff_acc SET status_staff='rejected' WHERE id_staff=%s"
    cursor.execute(sql, (staff_id,))
    connection.commit()

    flash("Staff has been rejected")
    return redirect(url_for("admin_dashboard_staff"))

@app.route("/admin_dashboard_staff_delete", methods=['POST'])
def admin_dashboard_staff_delete():
    staff_id = request.form.get("staff_id")
    sql = "DELETE FROM staff_acc WHERE id_staff=%s"
    cursor.execute(sql, (staff_id,))
    connection.commit()

    flash("Successfully deleted!")
    return redirect(url_for("admin_dashboard_staff"))



# ====================== staff page ======================

@app.route("/staff_home_page")
def staff_home_page():
    if "staff_id" not in session:
        return render_template("landing_page.html")

    staff_id = session["staff_id"]
    cursor.execute("SELECT * FROM staff_acc WHERE id_staff=%s", (staff_id,))
    staff = cursor.fetchone()

    return render_template("staff_home_page.html", staff=staff)


@app.route("/staff_profile", methods=["GET", "POST"])
def staff_profile():
    staff_id = session["staff_id"]

    if "staff_id" not in session:
        return redirect(url_for("staff_login"))

    if request.method == "POST":
        staff_photo = request.files.get('photo_staff')
        staff_name = request.form.get('name_staff')
        staff_email = request.form.get('email_staff')
        staff_phone = request.form.get('phone_staff')
        staff_pass = request.form.get('pass_staff')

        if staff_photo and staff_photo.filename != "":
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], staff_photo.filename)
            staff_photo.save(photo_path)

            staff_pic = "profile_p/" + staff_photo.filename

            sql = "UPDATE staff_acc SET profile_staff=%s, name_staff=%s, email_staff=%s, phone_staff=%s, pass_staff=%s WHERE id_staff=%s"
            cursor.execute(sql, (staff_pic, staff_name, staff_email, staff_phone, staff_pass, staff_id,))

        else:
            sql = "UPDATE staff_acc SET name_staff=%s, email_staff=%s, phone_staff=%s, pass_staff=%s WHERE id_staff=%s"
            cursor.execute(sql, (staff_name, staff_email, staff_phone, staff_pass, staff_id,))
        
        connection.commit()

        flash("Successfully updated!")
        return redirect(url_for("staff_profile"))

    sql = "SELECT * FROM staff_acc WHERE id_staff=%s"
    cursor.execute(sql, (staff_id,))
    staff = cursor.fetchone()

    return render_template("staff_profile.html", staff=staff)


#staff sign-up
@app.route("/staff_signup")
def staff_signup():
    return render_template("staff_signup.html")

@app.route("/staff_account", methods=["POST"])
def staff_account():
    staff_name = request.form.get('name_staff')
    staff_email = request.form.get('email_staff')
    staff_pass = request.form.get('pass_staff')

    sql = "INSERT INTO staff_acc (name_staff, email_staff, pass_staff, status_staff) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (staff_name, staff_email, staff_pass, "pending"))
    connection.commit()

    return redirect(url_for('staff_login'))


#staff_Login
@app.route("/staff_logout")
def staff_logout():
    session.pop("staff_id")
    flash("You have been logged out.")
    return redirect(url_for("staff_login"))

@app.route("/staff_login")
def staff_login():
    return render_template("staff_login.html")

@app.route("/login_process", methods=['POST'])
def login_process():
    staff_email = request.form.get("email_staff")
    staff_pass = request.form.get("pass_staff")

    sql = "SELECT * FROM staff_acc WHERE email_staff=%s AND pass_staff=%s"
    cursor.execute(sql, (staff_email, staff_pass))
    account_found = cursor.fetchone()

    if account_found:
        if account_found["status_staff"] == "approved":
            session["staff_id"] = account_found["id_staff"]
            return redirect(url_for("staff_home_page"))
        elif account_found["status_staff"] == "pending":
            flash("Your account is still pending approval from the admin.")
            return redirect(url_for("staff_login"))
        elif account_found["status_staff"] == "rejected":
            flash("Your account has been rejected. Contact admin for details.")
            return redirect(url_for("staff_login"))
    else:
        flash("Wrong Email Address or Password")
        return redirect(url_for("staff_login"))
    
#Staff Book List

@app.route("/booklist_staff", methods=["GET"])
def booklist_staff():
    if "staff_id" not in session:
        return render_template("landing_page.html")
    
    search = request.args.get("search", "")
    course = request.args.get("course", "")

    sql = "SELECT * FROM book_list WHERE 1=1"
    params = []

    if search:
        sql += " AND (title_book LIKE %s OR author_book LIKE %s)"
        params.extend([f"%{search}%", f"%{search}%"])

    if course and course != "ALL":
        sql += " AND course_book = %s"
        params.append(course)

    sql += " ORDER BY title_book ASC"

    cursor.execute(sql, params)
    books = cursor.fetchall()

    staff_id = session["staff_id"]
    cursor.execute("SELECT * FROM staff_acc WHERE id_staff=%s", (staff_id,))
    staff = cursor.fetchone()

    return render_template("booklist_staff.html", books=books, search=search, course=course, staff=staff)

@app.route("/book_details_staff")
def book_details_staff():
    if "staff_id" not in session:
        return render_template("landing_page.html")
    
    book_id = request.args.get("book_id")
    sql = "SELECT * FROM book_list WHERE id_book=%s"
    cursor.execute(sql, (book_id,))
    book = cursor.fetchone()
    
    staff_id = session["staff_id"]
    cursor.execute("SELECT * FROM staff_acc WHERE id_staff=%s", (staff_id,))
    staff = cursor.fetchone()

    return render_template("book_details_staff.html", staff=staff, book=book)



#staff_dashboard

@app.route("/staff_dashboard", methods=["GET"])
def staff_dashboard():
    if "staff_id" not in session:
        return render_template("landing_page.html")
    
    book_borrow = request.args.get("book_borrow", "") 
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT s.*, b.title_book, b.author_book, b.photo_book, b.course_book, b.year_book, b.quantity_book FROM student_list s LEFT JOIN book_list b ON s.book_borrow = b.title_book ORDER BY s.id_student DESC")
    std = cursor.fetchall()

    staff_id = session["staff_id"]
    cursor.execute("SELECT * FROM staff_acc WHERE id_staff=%s", (staff_id,))
    staff = cursor.fetchone()

    return render_template("staff_dashboard.html", std=std, staff=staff, book_borrow=book_borrow, today=today)




@app.route("/staff_dashboard_input", methods=["POST"])
def staff_dashboard_input():
    if "staff_id" not in session:
        return render_template("landing_page.html")

    namelast_student = request.form.get("namelast_student")
    namefirst_student = request.form.get("namefirst_student")
    course_student = request.form.get("course_student")
    email_student = request.form.get("email_student")
    phone_no = request.form.get("phone_no")
    book_borrow = request.form.get("book_borrow")
    return_borrow = request.form.get("return_borrow")

    date_borrow = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM book_list WHERE title_book=%s", (book_borrow,))
    book = cursor.fetchone()

    if not book:
        flash("Book not found in the library!")
        return redirect(url_for("staff_dashboard"))

    if book["quantity_book"] <= 0:
        flash("This book is currently unavailable.")
        return redirect(url_for("staff_dashboard"))

    new_quantity = book["quantity_book"] - 1
    new_status = "unavailable" if new_quantity == 0 else "available"

    cursor.execute("UPDATE book_list SET quantity_book=%s, status_book=%s WHERE id_book=%s", (new_quantity, new_status, book["id_book"]))
    connection.commit()

    cursor.execute("INSERT INTO student_list (namelast_student, namefirst_student, course_student, email_student, phone_no, book_borrow, date_borrow, return_borrow, status_borrow) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (namelast_student, namefirst_student, course_student, email_student, phone_no, book_borrow, date_borrow, return_borrow, "Borrowed"))
    connection.commit()

    flash("Borrow record added successfully!")
    return redirect(url_for("staff_dashboard"))



@app.route("/staff_dashboard_mod", methods=['POST'])
def staff_dashboard_mod():
    button_pressed = request.form.get('action_button')
    student_id = request.form.get('student_id')

    if button_pressed == "update_button":
        return redirect(url_for('staff_dashboard_mod_update', std_id=student_id))
    
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT book_borrow FROM student_list WHERE id_student = %s", (student_id,))
        borrowed_book = cursor.fetchone()

        if borrowed_book:
            book_title = borrowed_book['book_borrow']

            cursor.execute("UPDATE book_list SET quantity_book = quantity_book + 1, status_book = 'available' WHERE title_book = %s", (book_title,))
        
        cursor.execute("DELETE FROM student_list WHERE id_student = %s", (student_id,))
        connection.commit()
        cursor.close()

        flash("Book returned!")
        return redirect(url_for('staff_dashboard'))
    
@app.route("/staff_dashboard_mod_update")
def staff_dashboard_mod_update():
    if "staff_id" not in session:
        return render_template("landing_page.html")

    staff_id = session["staff_id"]
    cursor.execute("SELECT * FROM staff_acc WHERE id_staff=%s", (staff_id,))
    staff = cursor.fetchone()

    student_id = request.args.get('std_id')
    sql = "SELECT * FROM student_list WHERE id_student=%s"
    cursor.execute(sql, (student_id,))
    result = cursor.fetchone()

    flash("Information successfully updated!")
    return render_template('staff_dashboard_update.html', student_data=result, staff=staff)


#staff_dashboard_editing
@app.route("/staff_dashboard_mod_editing", methods=['POST'])
def staff_dashboard_mod_editing():

    studentid = request.form.get('id_student')
    namelast = request.form.get('namelast_student')
    namefirst = request.form.get('namefirst_student')
    course = request.form.get('course_student')
    email = request.form.get('email_student')
    contact = request.form.get('phone_no')
    date = request.form.get('date_borrow')
    returndate = request.form.get('date_return')
    book_borrowed = request.form.get('book_borrow')

    sql = "UPDATE student_list SET namelast_student=%s, namefirst_student=%s, course_student=%s, email_student=%s, phone_no=%s, book_borrow=%s, date_borrow=%s, return_borrow=%s WHERE id_student=%s"
    cursor.execute(sql, (namelast, namefirst, course, email, contact, book_borrowed, date, returndate, studentid))
    connection.commit()
    
    return redirect(url_for('staff_dashboard'))






if __name__ == "__main__":
    app.run(debug=True)