'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync').create();

var directoryjs = './medical_prescription/**/*.js'
var directorycss = './medical_prescription/**/*.css'
var directoryhtml = './medical_prescription/**/*.html'

gulp.task('browserSync', function() {
  browserSync.init({
    open: false,
    notify: false,
    proxy: 'localhost:8000'
  })
});

gulp.task('watch', function() {
  gulp.watch(directoryjs, browserSync.reload);
  gulp.watch(directoryhtml, browserSync.reload);
  gulp.watch(directorycss, browserSync.reload);
});

gulp.task('default',['browserSync', 'watch']);
