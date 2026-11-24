---
layout: default
title: FAQ
permalink: /faq.html
---

<section class="title" markdown="1">

# FAQ

</section>

<section class="plain" markdown="1">

### Q: Why is this FAQ only available in Chinese?

Sorry. No time for more translation :)

### Q: 我覺得很好用！

謝謝，你可以幫忙推廣，網址是 [http://ntu.csie.org/~piaip/pietty/](http://ntu.csie.org/~piaip/pietty/) ， 或是可以[贊助我個人](http://ntu.csie.org/~piaip/donate/)。

### Q: 我希望加上 XXXX 的功能...

請先查我的 計畫方向 (plans) 與 進行中的修改(todo list)。 若沒有你可以來信建議， 適合的我會加入，但不保證會實作。 如果是優先權比較低的項目可能是我覺得 不重要或太難做，你可以試著用donate 的方式來讓我改變優先權 :)

### Q: 我用 pputty、不想換成 PieTTY，可是又聽說有安全漏洞，怎麼辦?

因為太多人有這個需求，所以最後我還是製作了 pputty 0.2.4 ，與 0.2.3 的差異只在把 PuTTY 那兩個安全性修正加上去。

### Q: PuTTY, pputty, PieTTY 的關係

關於修正 PuTTY 的計畫， 早期有 [mhsin](http://www.mhsin.org/putty/) 製作的 DBCS patch 跟我 (piaip) 的透明與中文版， 但 PuTTY 越新的版本似乎反而問題越多； 這是因為 PuTTY 官方開發團隊決定以萬國碼 Unicode 的環境為主， 對於其它如 CJK 的 Big5 等字元的支援則採放棄狀態。 一部份原因是他們不熟悉非英語系的環境， 一方面是他們不願貿然採用大幅度改變結構的修正。

所以雖然我送了不少修正給官方版 PuTTY， 但許多對 CJK 亞洲語系的重大修正牽涉甚廣以至於他們不想貿然使用， 於是在 2004 年夏天我開始了 pputty 計畫， 目標是加上我想要的功能與修正，以及讓 PuTTY 對多國語系的支援達到 CJK 使用者的預期。

pputty 一開始時是一堆 hack 的集合，程式碼改得雜亂無章； 於是我決定在 0.23 版後全部重新改寫，也就是 PieTTY 。

### Q: 跟原始 PuTTY 有什麼不同？

原本我只是要解決 PuTTY 配合 新注音選字時會一次跳兩格 的問題，後來為了 想用英文字型且同時又能打中文 所以又做了 一個 patch。 最後我實在 不滿意它的 UI 所以修改了一套簡單化的界面， 就稱之為 pietty/pputty 界面吧。 我相信這樣的界面對一般初學者來說應該比原始 PuTTY 好上手。 簡單的說，連線畫面簡化了、提供選單列、方便調字型、自動儲存設定、...

### Q: PieTTY 與 pputty 又有什麼不同？

同樣是改進 PuTTY 的版本，簡單說 pputty 自 0.23 後重寫過就變成了 PieTTY 0.3 。 PieTTY 是全部重寫過的，且 PuTTY 已改變許多(中文問題更多了)， (很大原因是 PuTTY 發行了 0.57 所以 PieTTY 也只好一起發表新版) 所以剛開始發行的 PieTTY 暫時沒加入一些功能， 而把全部的精神放在架構與界面的重新設計、還有中文相容的各種問題上。 但自 0.3.11 起已完整的實作了包括 SCP 上傳的所有 pputty 的功能。

PieTTY 還加上了輕易切換字元編碼(encoding) 的設計，對 CJK 語系及 UTF-8 的支援尤其不錯，所以很建議您更換 pputty 到 pietty 。

### Q: 為什麼不把修正送回給原始 PuTTY 作者呢?

事實上一開始我有試著這樣做，我也早就寄信給他們了，可是 PuTTY Team 一開始都不理我。 新功能不談，嚴重的新注音 bug 也不修。 無奈之下我只好自己開始自己的版本 "pputty"。

事隔多年後，當 PieTTY 已經發展到很完整的階段後， PuTTY Team 終於有了回應... 據說因為很難測試 加上我沒寫清楚 patch 的原因與細節所以他們沒處理我送去的 CJK patch。 (CJK三國各自都有做自己版本的 PuTTY 不是沒有原因的... 日本也這樣，韓國也這樣) 於是我重新又送了三個重大的 CJK patch (新注音、覆疊視窗、IME字型)過去。

2005/03/21, PuTTY 回應說他們確認並 commit 覆疊視窗 跟 IME 字型的 bug 了，不過新注音 patch 還待確認。

2005/03/23, 經過多次 email 討論後，新注音等 patch 已全進入官方 PuTTY。 不過關於 DBCS 的游標畫字閃爍等問題，PuTTY Team 的態度是他們認為 UTF8 的支援比較重要，而這些在 UTF8 不會有問題。 由於使用我的 patch 牽涉甚大，可以肯定的是短期內不會進官方版 PuTTY。 所以，對於使用非 UTF8 的 DBCS 字集的人... PieTTY 可能仍然是你最好的選擇 ^^;

### Q: PieTTY 那一堆「亞洲語系修正」是做什麼用的？看不懂？

簡單說就是所有對中日等語言的修正。 平時建議您把 「建議開啟修正」下面的選項全打開，而 「選用性修正」則視情況。 分項解釋如下：

**「使用 Big5-2003 + 中國海字集」**

開啟後就可在未裝所謂「Unicode 補完」的系統上 正確的打入 big5 日文假名符號等，不懂的人可以去 巴哈姆特BBS 看看就會明白了。

**「內部轉換為 Unicode 處理」**

這可以說是歷史性的選項。 早期 PieTTY 對非 Unicode 處理的還不好時，由於 PuTTY 本身對 Unicode 的處理還不錯， 所以就產生了這個模式，把輸入的非 Unicode 字元直接轉換成 Unicode 內碼處理。 這種方式有好有壞，好處是 PuTTY/PieTTY 處理字元的行為會更正確，但缺點是遇到錯誤的字碼時會爛得很徹底， 所以會對某些人造成困擾。 但在新版的 PieTTY 上，這個選項 可說沒有開啟的必要了。

**「模擬24行終端機」**

24行終端機這選項則是因為某些 BBS 改寫不用 tty 時沒完整支援 telnet protocol, 結果就直接預設 terminal size 為24 行... 在這種 BBS 上看文章時最後不到一頁的捲動就會壞掉。 (PTT 在非 ssh 的模式就有這問題)，不過一般正常支援大 terminal 的系統則不用這種鬼東西... (註: 後來我寫了個 patch 叫 PTT 把這個問題改掉了，謝天謝地)

**「轉換 \\ 為日元符號」**

日本把一般打出來的 \\ 定為日元符號(YEN)。 PuTTY 本來的解決方法造成非日文使用者打 \\ 會看到很醜很怪的符號， 所以我用另一種方式來處理。這個選項大概只有日文使用者會想開。

### Q: SCP 怎麼只有上傳？

事實上可以下傳，但我還沒把界面寫出來。 沒那麼急的因素是，下傳通常可以用 http 之類的幫忙 ， (通常一般 ssh 登入的主機很多都有 www) 主要是上傳沒有，所以我寫了上傳。 有個問題是如果不能瀏覽的 SCP 好做但不好用，可以瀏覽的 SFTP 界面要花 超多時間來做且速度較慢。

註：後來覺得太麻煩，現在0.4+都沒有SCP了。

### Q: 可以直接開鏈結的話多好...

自 0.2.2 起已經可以了。

### Q: 一字雙色呢？

一字雙色是邪惡的東西... 而且容易大幅降低效率，所以 我討厭它 :)。 不過因為實在太多人問了，或許我哪天想不開會去做。

後記：我弄了個 hack 暫時解決一字雙色 (不會顯示雙色，但也不會讓字變問號了，只是 utf8 等會爛)， 不過偉大的 MichaelHsin 說他過幾天會來修這個 bug，那我就不弄了，期待他的大作 :)

再後記: 結果還是自己來... PieTTY 0.3.21 後開始支援一字雙色。

### Q: ANSI 碼剪貼、ANSI 編輯器、自動重試連線登入、分頁...

呃，這類非常 BBS 導向的問題我會放在最後處理。 PuTTY 比其它軟體強大的地方在於它對標準支援非常好， 所以我登入各種 UNIX 主機用它又快又正確，而 BBS 通常標準都亂做 (我可以找到 ptt bbs 的人幫我背書這事^^;) ，所以不會是我改 PuTTY 的主要方向。 分頁是個比較獨立的議題，我本身拿 PuTTY 是連到工作站用，所以都用 screen， 一個窗就夠了。 PuTTY 的架構確實也是改多窗超麻煩。 所以同樣等我哪天發呆太久覺得無聊才可能去做。

</section>

<section class="plain" markdown="1">

### Q: PieTTY 不是號稱可以顯示多國語言？ 怎麼我還是跑出方塊來？

為求效率， PieTTY 預設只會使用你系統的預設字型顯示設定， (如在一般中文 Windows 上多半系統設定為可顯示中日文， 但韓文則會顯示為方塊或空白; 若設定系統預設為英文模式， 可能連中文都變方塊了);

若要同時顯示更多種文字而在你的系統上會顯示出方塊或無法顯示， (當然前提是你要有正確的字型) 你可以重新設定字型或是使用 PieTTY 選項內的 "Multilingual Engine (多國語言顯示方式)" 設定，目前提供 Uniscribe 跟 MLang 兩種， 速度及效果各有不同，請照您的需求選用。

Uniscribe 的速度比較快，可是配某些字型似乎會發生大小不太合的狀況； MLang 是最慢的，但它的效果比 Uniscribe 好一些。

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

未開啟Multilingual

</div>

<div class="col" markdown="1">

![]({{ "/assets/images/faq-1-1e2cc2a1.png" | relative_url }})

</div>

<div class="col" markdown="1">

開啟Multilingual

</div>

<div class="col" markdown="1">

![]({{ "/assets/images/faq-2-a7a972cf.png" | relative_url }})

</div>

</div>

</section>

<section class="plain" markdown="1">

### Q: Unicode 補完 ！難道你沒看過 [「Unicode補完計畫 ─ 你真的知道它在做什麼嗎？」](http://ku.myftp.org/index_2005Q1.htm#18) 嗎？

我知道，而且我仔細思考過這個問題。

在 [Wikipedia](http://zh.wikipedia.org/wiki/Unicode%E8%A3%9C%E5%AE%8C%E8%A8%88%E7%95%AB)上曾看過這樣經典的說法: **『 於是這反而與「Unicode補完計畫」的創立宗旨背道而馳： 原先避免以外字集解決缺字的「Unicode補完計畫」，反而變成了另一套外字集。』**

真是說的太好了，雖然這不一定是該計畫小組的錯， (不管怎麼說，我們不應該全盤否定 Unicode 補完計畫的開發團隊， 他們真的有很偉大的貢獻) 但現實中它已帶來了不少問題。 Big5 是一套問題非常多的編碼方式， 而其中日文假名的問題更是大。 同樣是我所參與的計畫，但 PieTTY 與 Mozilla/ Firefox 我卻選了不同的解決方式，原因是這樣的:

**首先，日文假名到底是不是正常 Big5 所該有的字元？**

請參照[Big5-2003](http://www.cns11643.gov.tw/web/big5/)， Big5 日文假名雖然在 Windows(CP950) 中有保留為 Big5 區，但它並沒有對應到 日文區，而是設為造字區，這就是一切問題的根源。 在 Firefox 開始支援Big5日文假名前，由於 Big5 的標準混沌未明，就算要支援 也無所根據； 另外由於早期 Unicode 並不流行，許多人已用櫻花輸入法寫了 不少 Big5 日文的網頁。 考慮到一般人常用的問題、還有香港的 Big5-hkscs 已有把 Big5 日文做正確的對映；加上那時 openi18n-big5 制定的 TW-Big5 的出現 (可算是 Big5-2003 的前身，它算是台灣官方對 Big5 的定義表) ，所以 Mozilla/Firefox 就用 TW-Big5 (Big5-2003) 的名義重新編修了 Big5 的內碼對照表 (see bugzilla #9686)。 唯一的缺點是非 big5-2003 的系統會看不到以 Mozilla/Firefox 發出的表單或文章內的日文假名 (HTTP/HTML 的設計上其實若本來我們沒支援 Big5-2003 的話， 這些日文假名會轉為 unicode 表示方式，所以反而大家都看得到)。

**所以，Mozilla/Firefox 支援 Unicode 補完計畫？**

不，正如我前面所說， Mozilla/Firefox 支援的是台灣官方的 Big5-2003。 Unicode 補完計畫後來增加了很多簡體字跟日文漢字的對應， 最後甚至有部份與 Big5-2003 不相容的部份。 這也就是為什麼後來有人持續的做著非官方的 Unicode 補完版 Firefox。 但因為 Mozilla/Firefox/HTTP/HTML 是天生就可以處理 Unicode 的軟體/標準， (不加那些字碼時，本來反而其實大家都看得到， 加了後變只有同樣有加的人才看得到) 我們不應該隨便增加 Big5 的範圍。 所以我很堅持官方版 Firefox 不應該 隨便就把 Unicode-at-on(即Unicode 補完計畫) 的其它字集放進去， 除非官方 Big5 標準有修訂。 非官方版的，就當是某些人的特殊需求了。

<span class="green">註: 我與 UAO 的 witchfive 正在合作製作新的 Big5 字碼表 (希望能進 Firefox 1.5), 使用最大字集的輸入表(B » U) - Big5-2003+UAO2.41, 並使用最小字集的輸出表 (U » B) - CP950 + 最小修正， 這個版本理論上可完全正確的讀入 UAO 的字集，但又不會製造 UAO 的字， 有助於消減 UAO 在網路上繼續成長； 希望能通過。</span>

**那 PieTTY? 為什麼 PieTTY 不只支援 Big5-2003?**

PieTTY 用的環境是 Telnet/SSH。 這個世界多半是 ANSI/Multibyte Based 而非 Unicode。 就像我前面說的， HTTP/HTML 上對於使用中字元集無法編碼 的字仍有使用 unicode 的表示方法，但 telnet/SSH 沒有。 是以，對 telnet 的世界，如果你硬是要塞 Big5-2003 之外的字進去，別人**沒有** 任何正確方法可看到對應的字。 既然是這樣， PieTTY 乾脆把整個 Unicode-at-on (即 Unicode 補完計畫) 包進來，反正別人也沒別的方法看到。 不過 PieTTY 輸出時則是很正確的全轉成 Unicode，所以問題不太多。 唯一的問題是如果你用 PieTTY 遠端編輯文件時打了非傳統 Big5 的字， 而這個文件又是像 HTML 之類的東西的話，那就會造成跟前面一樣的問題。 話說回來... 對一個 Big5 的連線打了非 Big5 的字，這是無解的， 所以 PieTTY 支不支援 Unicode 補完計畫字集，都不影響。 (不裝 Unicode 補完字集的別人都一律看不到)。

**裝 Unicode 補完計畫就好了呀？ 那為何還要 PieTTY?**

有幾個原因: 首先，裝 Unicode-at-on 要管理者權限，又要重開機。 再來，有的軟體/標準本身就能處理 Unicode (如 HTML/HTTP)， 所以 Unicode-at-on 那種影響整個系統的方式有時會造成反效果。 以現在常用的 Windows XP 來說，它本身的 Unicode 支援就不錯， 一般常見上網需求除了 Telnet/SSH 仍是 ANSI 外，其它各種協定軟體多半 都是有 Unicode 的，所以 PieTTY 選擇支援 Unicode 補完計畫， 讓人可以只滿足這部份的需求。

</section>

<section class="plain" markdown="1">

### Q: 你根本不懂 telnet 吧，為什麼要選 PuTTY? xxMAN 好多了...

正好相反，我想我是有資格講話的，各大 terminal software 我大概都玩過， 國內國外從 NetTerm, ptelnet, BBSTerm, MultiTerm, ... 以前我還寫過完整的評鑑， 後來自己寫了一隻 pssh/ytelnet ， 再後來賣給 KKMan(所以我是少數有立場可以說 KKMAN 怎樣怎樣的人), ... 我想我比很多只能事後背歷史的人強多了，起碼在大學時期， 台灣 BBS 的演進過程我可是參與並影響不少的。 不過這已經是老人講古了... 一直到後期所謂 PCMan 一類出現時我已經淡出了， 回頭看這些連線軟體的戰爭我無意再去筆戰，你覺得別的軟體好就去用別的吧 :)

那麼為什麼用 PuTTY 呢？ 因為自己寫過、深知上面幾種軟體的缺點 (就我所需的用途來定義的缺點) 、再加上 Open Source 與免安裝的好處， 我覺得它夠完整，只是界面不好上手。 所以我以修改 putty 為主。

有人問我上面所謂缺點是哪些？ 以我的需求來說: (1) SSH. (2) Good vt100+xterm support for both display and kbd input, like PageUp. (3) fully implemention of RFC telnet protocol. Most TW terms cannot work with FreeBSD 4.X. (4) No "install" process, small and standalone. (5) Large and wide terminal , like 90x50 (6) Fast rendering (7) better if open source.

很大的因素是我用這種軟體不是拿來只玩 BBS 的，我需要拿來跟各種 (UNIX mostly) 系統連線，所以半調子的 terminal support 是不行的。 別的不說， 滿螢幕的超大 TERM 目前常看到的幾隻程式都處理的不好 (netterm 除外)。 SSH 跟免費+open source當然也是重要因素。 Open source 好處就在於作者不理你時 可以自己重做一隻，就像我現在一樣...

</section>

<section class="plain" markdown="1">

### 你 Close Source! 這樣不行啊！

目前 pputty final(0.2.4) 的 source 已經在 [下載頁]({{ "/download.html" | relative_url }}) 可抓到了。 PieTTY 要等我把想改的功能改完、穩定了之後再提供。 這是由於我想要集中 bug report, 並且減少因不同 build 產生的無用 bug report。 (過去的經驗是開放 download source 後常有人 build 不出來或自己亂改弄爛後又拿來 bug report, 這樣太浪費時間，所以在有穩定版本前不打算釋出 source)。

有個要給某些 Open Source 狂熱者的說明: PuTTY 使用的是 MIT License 而非 GPL, 所以我本來就沒有必要把新的 patch 放出來。 由於某些 Open Source 蟑螂的行為讓我很反感， 所以完整 PieTTY 的存取權我目前只打算開放給我認可的開發者（目前已有超過五人以上可以存取 PieTTY 的 source）。 CJK 相關的修正則是會送回給 PuTTY team。

### pputty 的 License 是？

跟 PuTTY 一樣使用 [MIT License (GPL Compatible)](http://www.chiark.greenend.org.uk/~sgtatham/putty/licence.html)，大意是你可以任意使用它的任何部份。

### pputty 有源碼 Source 可以抓嗎？

我會以 diff-patch 的形式發行，因為我希望能一直使用最新的 PuTTY 做 backend。 但每隔一段時間才會整理。 目前已提供 pputty 0.2.4 final 的源碼，請至下載頁下載。

</section>
