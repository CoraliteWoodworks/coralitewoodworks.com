/* jquery.scrollzer v0.2 | (c) @ajlkn | MIT licensed */
jQuery.scrollzer = function (e, t) {
    var r = jQuery(window), a = jQuery(document);
    r.load(function () {
        var i, o, s, l, n, c,
            u = jQuery.extend({activeClassName: "active", suffix: "-link", pad: 50, firstHack: !1, lastHack: !1}, t),
            d = [], f = jQuery();
        for (i in e) s = jQuery("#" + e[i]), l = jQuery("#" + e[i] + u.suffix), s.length < 1 || l.length < 1 || (o = {}, o.link = l, o.object = s, d[e[i]] = o, f = f.add(l));
        var v, h = function () {
            var e;
            for (i in d) e = d[i], e.start = Math.ceil(e.object.offset().top) - u.pad, e.end = e.start + Math.ceil(e.object.innerHeight());
            r.trigger("scroll")
        };
        r.resize(function () {
            window.clearTimeout(v), v = window.setTimeout(h, 250)
        });
        var j, m = function () {
            f.removeClass("scrollzer-locked")
        };
        r.scroll(function (e) {
            var t = 0, o = !1;
            n = r.scrollTop(), window.clearTimeout(j), j = window.setTimeout(m, 250);
            for (i in d) i != c && n >= d[i].start && n <= d[i].end && (c = i, o = !0), t++;
            u.lastHack && n + r.height() >= a.height() && (c = i, o = !0), o && !f.hasClass("scrollzer-locked") && (f.removeClass(u.activeClassName), d[c].link.addClass(u.activeClassName))
        }), r.trigger("resize")
    })
};
