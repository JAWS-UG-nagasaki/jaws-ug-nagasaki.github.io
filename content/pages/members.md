Title: メンバー
Date: 2026-05-23
Save_as: members.html

# メンバー

JAWS-UG 長崎の運営メンバーをご紹介します。

{% if site_members %}
<div class="members-grid">
{% for member in site_members %}
<div class="member-card">
    <img src="{{ member.avatar }}" alt="{{ member.name }}" class="member-avatar">
    <div class="member-name">{{ member.name }}</div>
</div>
{% endfor %}
</div>
{% else %}
<p>メンバー情報を登録してください。</p>
{% endif %}

<style>
.members-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}
.member-card {
    text-align: center;
    padding: 1.5rem;
    background: #353435;
    border-radius: 0.5rem;
}
.member-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
}
.member-name {
    font-size: 1.125rem;
    font-weight: 600;
    color: #e5e2e2;
}
</style>
