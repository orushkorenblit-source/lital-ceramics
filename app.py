import streamlit as st
import urllib.parse  # ספרייה מובנית בפייתון שמאפשרת להפוך טקסט לקישור אינטרנט תקין

# הגדרות דף - כותרת ועיצוב עם תמיכה מובנית בעברית
st.set_page_config(page_title="ליטל בכר - סטודיו לקרמיקה", layout="centered")

# עיצוב כותרת ראשית מעוצבת
st.markdown("<h1 style='text-align: center; color: #4e342e; direction: rtl;'>ליטל בכר - אמנות בחומר 🏺</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #795548; direction: rtl;'>סטודיו לקרמיקה במושב מכורה, בקעת הירדן</h3>", unsafe_allow_html=True)

st.divider()

# 1. תמונת Hero ראשית
try:
    st.image("images/hero.jpeg", caption="יוצרת בלב הבקעה - ליטל בכר", use_container_width=True)
except Exception:
    st.warning("⚠️ לא נטענה תמונת ה-Hero. ודאי שקראת לתמונה בשם hero.jpeg בתוך תיקיית images.")

st.divider()

# 2. אודות והזמנה לסדנאות במבנה עמודות נקי
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    st.markdown("### ✨ הקסם שבחומר")
    st.write("""
    נעים להכיר, שמי ליטל בכר. בסטודיו שלי במושב מכורה השקט, 
    אני הופכת חומר גלם ליצירות אמנות שימושיות וייחודיות.
    
    הסטודיו הוא מרחב של שקט, יצירה וחיבור לאדמה. אני מזמינה אתכם 
    להצטרף אלי למסע של חומר ורוח בלב הנוף המרהיב של בקעת הירדן.
    """)
    
    st.markdown("#### **מה קורה בסטודיו?**")
    st.write("""
    * **סדנאות זוגיות:** חוויה רומנטית ושקטה של יצירה משותפת.
    * **סדנאות לקבוצות וימי הולדת:** פעילות מגבשת ומהנה.
    * **שיעורים פרטניים:** למידה מעמיקה של עבודה על אובניים ופיסול ידני.
    * **מכירת תוצרת:** כלי בית, נוי ומתנות בעבודת יד.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    try:
        st.image("images/studio.jpeg", use_container_width=True)
    except Exception:
        st.write("(תמונת סטודיו)")

st.divider()

# 3. גלריית עבודות בשלוש עמודות
st.markdown("<h3 style='text-align: center; direction: rtl;'>מהתוצרים שלנו 📸</h3>", unsafe_allow_html=True)
img_col1, img_col2, img_col3 = st.columns(3)

with img_col1:
    try:
        st.image("images/item1.jpeg", use_container_width=True)
    except Exception:
        st.caption("🖼️ מוצר 1")

with img_col2:
    try:
        st.image("images/item2.jpeg", use_container_width=True)
    except Exception:
        st.caption("🖼️ מוצר 2")

with img_col3:
    try:
        st.image("images/item3.jpeg", use_container_width=True)
    except Exception:
        st.caption("🖼️ מוצר 3")

st.divider()

# 4. טופס יצירת קשר ושליחה לוואטסאפ
st.markdown("<h3 style='text-align: right; direction: rtl;'>📞 דברו איתי בוואטסאפ</h3>", unsafe_allow_html=True)

# שינוי כאן: הגדרת מספר הטלפון של ליטל (בפורמט בינלאומי בלי ה-0 בהתחלה ובלי מקפים, למשל 972501234567)
LITAL_PHONE = "972509022292"  # <-- החליפי למספר האמיתי של ליטל!

with st.form("contact_form"):
    st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)
    
    col_name, col_phone = st.columns(2)
    with col_name:
        name = st.text_input("שם מלא *")
    with col_phone:
        phone = st.text_input("טלפון שלכם *")
        
    subject = st.selectbox("במה אתם מתעניינים?", ["סדנה זוגית", "סדנה לקבוצה", "שיעורי קרמיקה", "רכישת כלים", "אחר"])
    message = st.text_area("הודעה נוספת (אופציונלי)")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    submit_button = st.form_submit_button("הכנת הודעת וואטסאפ")

# מחוץ לטופס - הטיפול בלחיצה
if submit_button:
    if name and phone:
        # בניית טקסט ההודעה שיופיע בוואטסאפ
        base_msg = f"היי ליטל! שמי {name} (טלפון: {phone}). אני מעוניין/ת בפרטים לגבי: *{subject}*."
        if message:
            base_msg += f" הווספתי גם הודעה: {message}"
        
        # המרה של הטקסט לפורמט של קישור אינטרנט תקין (קידוד רווחים וכדומה)
        encoded_msg = urllib.parse.quote(base_msg)
        
        # יצירת הקישור הסופי
        whatsapp_url = f"https://wa.me/{LITAL_PHONE}?text={encoded_msg}"
        
        # הצגת כפתור ירוק גדול ומרשים לשליחה
        st.success("ההודעה מוכנה! לחצו על הכפתור למטה כדי לשלוח אותה ישירות לוואטסאפ של ליטל:")
        st.link_button("🟢 מעבר לשליחה בוואטסאפ", whatsapp_url, use_container_width=True)
    else:
        st.error("בבקשה מלאו שם וטלפון כדי שנוכל להכין את הפנייה.")

st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 ליטל בכר - קרמיקה בעבודת יד | מושב מכורה</p>", unsafe_allow_html=True)